import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings

warnings.filterwarnings('ignore')


class ESGDataAnalyzer:
    def __init__(self, data_path):
        """初始化分析器"""
        self.df = None
        self.data_path = data_path
        self.setup_plot_style()
        self.load_data()

    def setup_plot_style(self):
        """设置绘图样式"""
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        plt.rcParams['font.size'] = 6
        plt.rcParams['xtick.labelsize'] = 6
        plt.rcParams['ytick.labelsize'] = 6
        plt.rcParams['legend.fontsize'] = 6
        plt.rcParams['axes.titlesize'] = 8
        plt.rcParams['axes.labelsize'] = 6

    def load_data(self):
        """加载和预处理数据"""
        print("正在加载数据...")
        self.df = pd.read_csv(self.data_path)

        # 日期处理
        self.df['AS_OF_DATE'] = pd.to_datetime(self.df['AS_OF_DATE'])
        self.df['IVA_RATING_DATE'] = pd.to_datetime(self.df['IVA_RATING_DATE'])

        # 提取时间特征
        self.df['YEAR'] = self.df['AS_OF_DATE'].dt.year
        self.df['MONTH'] = self.df['AS_OF_DATE'].dt.month
        self.df['YEAR_MONTH'] = self.df['AS_OF_DATE'].dt.to_period('M')

        # 评级映射
        self.rating_mapping = {'AAA': 10, 'AA': 9, 'A': 8, 'BBB': 7, 'BB': 6, 'B': 5,
                               'CCC': 4, 'CC': 3, 'C': 2, 'D': 1}

        # 支柱列定义
        self.pillar_columns = ['ENVIRONMENTAL_PILLAR_SCORE', 'SOCIAL_PILLAR_SCORE', 'GOVERNANCE_PILLAR_SCORE']
        self.pillar_names = ['环境', '社会', '治理']

        self._calculate_rating_changes()
        self.print_data_overview()

    def _calculate_rating_changes(self):
        """计算评级变化"""
        self.df['CURRENT_RATING_NUM'] = self.df['IVA_COMPANY_RATING'].map(self.rating_mapping)
        self.df['PREVIOUS_RATING_NUM'] = self.df['IVA_PREVIOUS_RATING'].map(self.rating_mapping)
        self.df['RATING_CHANGE'] = self.df['CURRENT_RATING_NUM'] - self.df['PREVIOUS_RATING_NUM']

    def print_data_overview(self):
        """打印数据概览"""
        print(f"\n数据时间范围: {self.df['AS_OF_DATE'].min()} 到 {self.df['AS_OF_DATE'].max()}")
        print(f"包含的公司数量: {self.df['ISSUER_NAME'].nunique()}")
        print(f"包含的国家数量: {self.df['ISSUER_CNTRY_DOMICILE'].nunique()}")
        print(f"包含的行业数量: {self.df['IVA_INDUSTRY'].nunique()}")

    def analyze_rating_distribution(self):
        """分析ESG评级分布"""
        print("\n=== ESG评级分布分析 ===")
        rating_distribution = self.df['IVA_COMPANY_RATING'].value_counts().sort_index()

        plt.figure(figsize=(15, 12))

        # 1.1 ESG评级分布饼图
        plt.subplot(2, 3, 1)
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57', '#FF9FF3']
        rating_distribution.plot(kind='pie', autopct='%1.1f%%', colors=colors)
        plt.title('ESG评级分布', fontsize=8)
        plt.ylabel('')

        return rating_distribution

    def analyze_rating_trends(self):
        """分析评级趋势"""
        print("\n=== ESG评级趋势分析 ===")

        # 按时间分析评级变化
        rating_trend = self.df.groupby(['YEAR', 'MONTH', 'IVA_COMPANY_RATING']).size().unstack(fill_value=0)

        plt.subplot(2, 3, 2)
        rating_trend.plot(kind='line', marker='o', markersize=3)
        plt.title('ESG评级随时间变化趋势', fontsize=8)
        plt.xlabel('时间', fontsize=6)
        plt.ylabel('公司数量', fontsize=6)
        plt.legend(title='ESG评级', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=6)
        plt.xticks(rotation=45, fontsize=6)
        plt.yticks(fontsize=6)

        return rating_trend

    def analyze_pillar_scores(self):
        """分析三大支柱得分"""
        print("\n=== 三大支柱得分分析 ===")

        # 3.1 各支柱平均得分
        pillar_scores = self.df[self.pillar_columns].mean()

        plt.subplot(2, 3, 3)
        pillar_scores.plot(kind='bar', color=['#4ECDC4', '#45B7D1', '#96CEB4'])
        plt.title('三大支柱平均得分', fontsize=8)
        plt.ylabel('平均得分', fontsize=6)
        plt.xticks(rotation=45, fontsize=6)
        plt.yticks(fontsize=6)

        # 3.2 支柱得分随时间变化
        plt.subplot(2, 3, 4)
        pillar_trend = self.df.groupby('YEAR_MONTH')[self.pillar_columns].mean()
        pillar_trend.plot(kind='line', marker='o', markersize=3)
        plt.title('三大支柱得分随时间变化', fontsize=8)
        plt.xlabel('时间', fontsize=6)
        plt.ylabel('平均得分', fontsize=6)
        plt.legend(self.pillar_names, fontsize=6)
        plt.xticks(rotation=45, fontsize=6)
        plt.yticks(fontsize=6)

        return pillar_scores, pillar_trend

    def analyze_industry_performance(self):
        """分析行业表现"""
        print("\n=== 行业ESG表现分析 ===")

        # 各行业平均ESG得分
        industry_scores = self.df.groupby('IVA_INDUSTRY')['INDUSTRY_ADJUSTED_SCORE'].mean().sort_values(ascending=False)

        plt.subplot(2, 3, 5)
        industry_scores.head(15).plot(kind='barh', color='skyblue')  # 限制显示数量
        plt.title('各行业平均ESG得分(前15)', fontsize=8)
        plt.xlabel('平均ESG得分', fontsize=6)
        plt.yticks(fontsize=6)
        plt.xticks(fontsize=6)

        return industry_scores

    def analyze_rating_changes(self):
        """分析评级变化"""
        print("\n=== 评级变化趋势分析 ===")

        rating_change_summary = self.df['RATING_CHANGE'].value_counts().sort_index()

        plt.subplot(2, 3, 6)
        rating_change_summary.plot(kind='bar',
                                   color=['red' if x < 0 else 'green' if x > 0 else 'gray'
                                          for x in rating_change_summary.index])
        plt.title('ESG评级变化分布', fontsize=8)
        plt.xlabel('评级变化 (负值=降级, 0=不变, 正值=升级)', fontsize=6)
        plt.ylabel('公司数量', fontsize=6)
        plt.xticks(fontsize=6)
        plt.yticks(fontsize=6)

        return rating_change_summary

    def create_detailed_analysis(self):
        """创建详细分析图表"""
        print("\n=== 详细趋势分析 ===")

        plt.figure(figsize=(15, 10))

        # 7.1 月度ESG得分趋势
        plt.subplot(2, 2, 1)
        monthly_scores = self.df.groupby('YEAR_MONTH')['INDUSTRY_ADJUSTED_SCORE'].mean()
        monthly_scores.plot(kind='line', marker='o', color='purple', linewidth=1, markersize=3)
        plt.title('月度平均ESG得分趋势', fontsize=8)
        plt.xlabel('时间', fontsize=6)
        plt.ylabel('平均ESG得分', fontsize=6)
        plt.xticks(fontsize=6)
        plt.yticks(fontsize=6)
        plt.grid(True, alpha=0.3)

        # 7.2 评级分布随时间变化
        plt.subplot(2, 2, 2)
        rating_over_time = pd.crosstab(self.df['AS_OF_DATE'], self.df['IVA_COMPANY_RATING'], normalize='index')
        rating_over_time.plot(kind='area', stacked=True, alpha=0.7)
        plt.title('ESG评级分布随时间变化', fontsize=8)
        plt.xlabel('日期', fontsize=6)
        plt.ylabel('比例', fontsize=6)
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=6)
        plt.xticks(fontsize=6)
        plt.yticks(fontsize=6)

        # 7.3 各行业ESG表现热力图
        plt.subplot(2, 2, 3)
        industry_rating_matrix = pd.crosstab(self.df['IVA_INDUSTRY'], self.df['IVA_COMPANY_RATING'], normalize='index')
        # 限制行业数量以避免过于密集
        top_industries = industry_rating_matrix.sum(axis=1).nlargest(10).index
        industry_rating_matrix = industry_rating_matrix.loc[top_industries]

        sns.heatmap(industry_rating_matrix, annot=True, cmap='YlOrRd', fmt='.2f',
                    annot_kws={"size": 5}, cbar_kws={"shrink": 0.8})
        plt.title('各行业ESG评级分布热力图(前10行业)', fontsize=8)
        plt.xlabel('ESG评级', fontsize=6)
        plt.ylabel('行业', fontsize=6)
        plt.xticks(rotation=45, fontsize=6)
        plt.yticks(fontsize=6)

        # 7.4 支柱得分相关性
        plt.subplot(2, 2, 4)
        correlation_matrix = self.df[self.pillar_columns].corr()
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0,
                    square=True, fmt='.2f', annot_kws={"size": 6}, cbar_kws={"shrink": 0.8})
        plt.title('三大支柱得分相关性', fontsize=8)
        plt.xticks(fontsize=6)
        plt.yticks(fontsize=6)

        plt.tight_layout()
        plt.show()

        return monthly_scores, industry_rating_matrix, correlation_matrix

    def create_theme_analysis(self):
        """创建主题分析图表"""
        plt.figure(figsize=(15, 10))

        # 环境主题得分分析
        plt.subplot(2, 2, 1)
        environmental_themes = ['CLIMATE_CHANGE_THEME_SCORE', 'NATURAL_RES_USE_THEME_SCORE',
                                'WASTE_MGMT_THEME_SCORE', 'ENVIRONMENTAL_OPPS_THEME_SCORE']
        env_theme_scores = self.df[environmental_themes].mean()
        env_theme_scores.plot(kind='bar', color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
        plt.title('环境主题平均得分', fontsize=8)
        plt.ylabel('平均得分', fontsize=6)
        plt.xticks(rotation=45, fontsize=6)
        plt.yticks(fontsize=6)

        # 社会主题得分分析
        plt.subplot(2, 2, 2)
        social_themes = ['HUMAN_CAPITAL_THEME_SCORE', 'PRODUCT_SAFETY_THEME_SCORE',
                         'SOCIAL_OPPS_THEME_SCORE']
        social_theme_scores = self.df[social_themes].mean()
        social_theme_scores.plot(kind='bar', color=['#1f77b4', '#ff7f0e', '#2ca02c'])
        plt.title('社会主题平均得分', fontsize=8)
        plt.ylabel('平均得分', fontsize=6)
        plt.xticks(rotation=45, fontsize=6)
        plt.yticks(fontsize=6)

        # 公司评级变化分布
        plt.subplot(2, 2, 3)
        company_rating_changes = self.df.groupby('ISSUER_NAME').agg({
            'RATING_CHANGE': 'mean',
            'IVA_COMPANY_RATING': 'last',
            'INDUSTRY_ADJUSTED_SCORE': 'mean'
        }).sort_values('RATING_CHANGE', ascending=False)

        top_improvers = company_rating_changes.head(10)['RATING_CHANGE']
        top_improvers.plot(kind='barh', color='green')
        plt.title('评级提升最多的公司(前10)', fontsize=8)
        plt.xlabel('评级变化', fontsize=6)
        plt.yticks(fontsize=6)
        plt.xticks(fontsize=6)

        # 国家ESG表现
        plt.subplot(2, 2, 4)
        country_scores = self.df.groupby('ISSUER_CNTRY_DOMICILE')['INDUSTRY_ADJUSTED_SCORE'].mean()
        country_scores = country_scores.sort_values(ascending=False).head(10)
        country_scores.plot(kind='bar', color='lightblue')
        plt.title('各国平均ESG得分(前10)', fontsize=8)
        plt.ylabel('平均ESG得分', fontsize=6)
        plt.xticks(rotation=45, fontsize=6)
        plt.yticks(fontsize=6)

        plt.tight_layout()
        plt.show()

        return company_rating_changes, country_scores

    def generate_summary_report(self):
        """生成分析总结报告"""
        print("\n=== 关键发现总结 ===")

        # 计算整体趋势
        overall_trend = self.df['RATING_CHANGE'].mean()
        improving_companies = len(self.df[self.df['RATING_CHANGE'] > 0])
        declining_companies = len(self.df[self.df['RATING_CHANGE'] < 0])
        stable_companies = len(self.df[self.df['RATING_CHANGE'] == 0])

        industry_scores = self.df.groupby('IVA_INDUSTRY')['INDUSTRY_ADJUSTED_SCORE'].mean()
        pillar_scores = self.df[self.pillar_columns].mean()

        print(f"整体评级变化趋势: {overall_trend:.2f}")
        print(f"评级提升的公司数量: {improving_companies}")
        print(f"评级下降的公司数量: {declining_companies}")
        print(f"评级稳定的公司数量: {stable_companies}")

        # 最佳和最差表现的行业
        best_industry = industry_scores.idxmax()
        worst_industry = industry_scores.idxmin()
        print(f"\nESG表现最佳的行业: {best_industry} (得分: {industry_scores.max():.2f})")
        print(f"ESG表现最差的行业: {worst_industry} (得分: {industry_scores.min():.2f})")

        # 支柱表现分析
        best_pillar = pillar_scores.idxmax()
        worst_pillar = pillar_scores.idxmin()
        print(f"\n表现最佳的支柱: {best_pillar} (得分: {pillar_scores.max():.2f})")
        print(f"表现最差的支柱: {worst_pillar} (得分: {pillar_scores.min():.2f})")

        # 保存分析结果
        summary_report = {
            '数据期间': f"{self.df['AS_OF_DATE'].min()} 到 {self.df['AS_OF_DATE'].max()}",
            '公司数量': self.df['ISSUER_NAME'].nunique(),
            '行业数量': self.df['IVA_INDUSTRY'].nunique(),
            '平均ESG得分': f"{self.df['INDUSTRY_ADJUSTED_SCORE'].mean():.2f}",
            '评级提升公司比例': f"{(improving_companies / len(self.df)) * 100:.1f}%",
            '评级下降公司比例': f"{(declining_companies / len(self.df)) * 100:.1f}%",
            '最佳行业': best_industry,
            '最差行业': worst_industry,
            '整体趋势': "改善" if overall_trend > 0 else "恶化" if overall_trend < 0 else "平稳"
        }

        print("\n=== 分析总结报告 ===")
        for key, value in summary_report.items():
            print(f"{key}: {value}")

        return summary_report

    def create_summary_chart(self):
        """创建总结图表"""
        plt.figure(figsize=(12, 8))

        # 评级分布总结
        plt.subplot(2, 2, 1)
        rating_counts = self.df['IVA_COMPANY_RATING'].value_counts()
        rating_counts.plot(kind='bar', color='lightblue')
        plt.title('ESG评级分布总结', fontsize=8)
        plt.xlabel('ESG评级', fontsize=6)
        plt.ylabel('公司数量', fontsize=6)
        plt.xticks(fontsize=6)
        plt.yticks(fontsize=6)

        # 评级变化总结
        plt.subplot(2, 2, 2)
        improving = len(self.df[self.df['RATING_CHANGE'] > 0])
        stable = len(self.df[self.df['RATING_CHANGE'] == 0])
        declining = len(self.df[self.df['RATING_CHANGE'] < 0])

        changes = [improving, stable, declining]
        labels = ['提升', '稳定', '下降']
        colors = ['green', 'gray', 'red']
        plt.bar(labels, changes, color=colors)
        plt.title('公司评级变化总结', fontsize=8)
        plt.ylabel('公司数量', fontsize=6)
        plt.xticks(fontsize=6)
        plt.yticks(fontsize=6)

        # 支柱得分对比
        plt.subplot(2, 2, 3)
        pillar_scores = self.df[self.pillar_columns].mean()
        pillar_scores.plot(kind='bar', color=['#4ECDC4', '#45B7D1', '#96CEB4'])
        plt.title('三大支柱得分对比', fontsize=8)
        plt.ylabel('平均得分', fontsize=6)
        plt.xticks(rotation=45, fontsize=6)
        plt.yticks(fontsize=6)

        # 时间趋势
        plt.subplot(2, 2, 4)
        monthly_scores = self.df.groupby('YEAR_MONTH')['INDUSTRY_ADJUSTED_SCORE'].mean()
        monthly_scores.plot(kind='line', color='purple', linewidth=1, marker='o', markersize=2)
        plt.title('ESG得分时间趋势', fontsize=8)
        plt.xlabel('时间', fontsize=6)
        plt.ylabel('平均ESG得分', fontsize=6)
        plt.xticks(rotation=45, fontsize=6)
        plt.yticks(fontsize=6)
        plt.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.show()

    def run_full_analysis(self):
        """运行完整分析流程"""
        print("开始ESG数据分析...")

        # 第一组图表：基础分析
        self.analyze_rating_distribution()
        self.analyze_rating_trends()
        self.analyze_pillar_scores()
        self.analyze_industry_performance()
        self.analyze_rating_changes()
        plt.tight_layout()
        plt.show()

        # 第二组图表：详细分析
        self.create_detailed_analysis()

        # 第三组图表：主题分析
        self.create_theme_analysis()

        # 总结报告和图表
        summary = self.generate_summary_report()
        self.create_summary_chart()

        return summary


# 使用示例
if __name__ == "__main__":
    # 初始化分析器
    analyzer = ESGDataAnalyzer('znttaqleyuk9pjxj.csv')

    # 运行完整分析
    results = analyzer.run_full_analysis()

    print("\n分析完成！")