# csmar_financial_analysis.py
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import warnings
import os

warnings.filterwarnings('ignore')
#忽略所有显示

#面向对象编程
class ESGDataAnalyzer:
    """ESG数据分析器"""
#面向对象编程
    def __init__(self, file_path='znttaqleyuk9pjxj.csv'):
        self.financial_data = None
        self.file_path = file_path
        self.setup_visualization()
#图像设置
    def setup_visualization(self):
        
        plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans', 'Arial']
        plt.rcParams['axes.unicode_minus'] = False
        plt.rcParams['figure.figsize'] = (16, 14)  # 增大默认图像尺寸，提供更多空间
        plt.rcParams['figure.dpi'] = 150  # 提高分辨率
        plt.rcParams['savefig.dpi'] = 300  # 保存图像时的分辨率
        plt.rcParams['font.size'] = 12
        plt.rcParams['axes.titlesize'] = 14
        plt.rcParams['axes.labelsize'] = 12
        plt.rcParams['xtick.labelsize'] = 10
        plt.rcParams['ytick.labelsize'] = 10
        plt.rcParams['legend.fontsize'] = 10
        plt.rcParams['figure.titlesize'] = 16
        print("可视化环境设置完成")
    #数据读取函数
    def load_local_data(self):
        #数据写入
        print("本地数据加载")

        try:
            # 检查文件是否存在，是否成功读取
            if not os.path.exists(self.file_path):
                print(f"文件不存在: {self.file_path}")
                print("请确保CSV文件在当前目录下")
                return False

            # 读取CSV文件，可能是编码的问题
            self.financial_data = pd.read_csv(self.file_path, encoding='utf-8')

            # 如果utf-8读取失败，尝试其他编码
            if self.financial_data.empty:
                print("⚠️ UTF-8编码读取失败，尝试GBK编码...")
                self.financial_data = pd.read_csv(self.file_path, encoding='gbk')

            #数据特征前瞻
            print(f"成功加载ESG数据: {len(self.financial_data)} 条记录")
            print(f"数据形状: {self.financial_data.shape}")
            print(f"字段数量: {len(self.financial_data.columns)}")

            # 显示数据基本信息
            print("\n🔍 数据基本信息:")
            print(f"数据列: {list(self.financial_data.columns)[:10]}...")  # 只显示前10列

            # 显示前几行数据
            print("\n数据预览:")
            print(self.financial_data.head(5).to_string(index=False))

            return True

        except Exception as e:
            print(f"❌ 加载本地文件失败: {e}")
            return False

    def explore_data_fields(self):
        #提前创建字符串
        print("\n" + "=" * 80)
        print("1. 探索ESG数据字段结构")
        print("=" * 80)
        
        if self.financial_data is None:
            print("❌没有可用的数据")
            return

        print(f"共有 {len(self.financial_data.columns)} 个字段")
        print(f"数据记录数: {len(self.financial_data)}")

        # 分类显示ESG字段
        self._categorize_esg_fields()

    def _categorize_esg_fields(self):
    
        field_names = self.financial_data.columns.tolist()

        #基础信息字段
        #通过关键词对field_name进行计数，筛选前15
        basic_fields = [f for f in field_names if
                        any(keyword in f.lower() for keyword in
                            ['issuer', 'name', 'date', 'country', 'industry', 'rating'])]
        print(f"\n 基础信息字段 ({len(basic_fields)}个):")
        for field in sorted(basic_fields)[:15]:
            print(f"  - {field}")

        # E(环境)相关字段
        env_fields = [f for f in field_names if
                      any(keyword in f.lower() for keyword in
                          ['environment', 'climate', 'carbon', 'energy', 'water', 'waste', 'biodiv'])]
        print(f"\n🌱 环境(E)相关字段 ({len(env_fields)}个):")
        for field in sorted(env_fields)[:15]:
            print(f"  - {field}")

        # S(社会)相关字段
        social_fields = [f for f in field_names if
                         any(keyword in f.lower() for keyword in
                             ['social', 'human', 'labor', 'health', 'safety', 'product', 'privacy'])]
        print(f"\n👥 社会(S)相关字段 ({len(social_fields)}个):")
        for field in sorted(social_fields)[:15]:
            print(f"  - {field}")

        # G(治理)相关字段
        gov_fields = [f for f in field_names if
                      any(keyword in f.lower() for keyword in
                          ['governance', 'board', 'committee', 'director', 'audit', 'ethics'])]
        print(f"\n🏛️ 治理(G)相关字段 ({len(gov_fields)}个):")
        for field in sorted(gov_fields)[:15]:
            print(f"  - {field}")

        # 评分字段
        score_fields = [f for f in field_names if 'score' in f.lower()]
        print(f"\n 评分字段 ({len(score_fields)}个):")
        for field in sorted(score_fields)[:20]:
            print(f"  - {field}")

    def identify_key_fields(self):
        #行业字段筛选
        print("\n" + "=" * 80)
        print("2. 识别关键ESG字段")
        print("=" * 80)

        if self.financial_data is None:
            print("❌ 没有可用的数据")
            return {}

        available_columns = self.financial_data.columns.tolist()
        key_fields = {}

        # 寻找公司名称字段
        name_fields = [col for col in available_columns if
                       any(keyword in col.lower() for keyword in
                           ['issuer_name', 'name', 'company'])]
        key_fields['name'] = name_fields[0] if name_fields else None
        print(f"公司名称字段: {key_fields['name']}")

        # 寻找日期字段
        date_fields = [col for col in available_columns if
                       any(keyword in col.lower() for keyword in
                           ['date', 'as_of_date', 'rating_date'])]
        key_fields['date'] = date_fields[0] if date_fields else None
        print(f"📅 日期字段: {key_fields['date']}")

        # 寻找评级字段
        rating_fields = [col for col in available_columns if
                         any(keyword in col.lower() for keyword in
                             ['rating', 'iva_company_rating'])]
        key_fields['rating'] = rating_fields[0] if rating_fields else None
        print(f"⭐ 评级字段: {key_fields['rating']}")

        # 寻找行业字段
        industry_fields = [col for col in available_columns if
                           any(keyword in col.lower() for keyword in
                               ['industry', 'iva_industry'])]
        key_fields['industry'] = industry_fields[0] if industry_fields else None
        print(f"🏭 行业字段: {key_fields['industry']}")

        # 寻找ESG总分字段
        total_score_fields = [col for col in available_columns if
                              any(keyword in col.lower() for keyword in
                                  ['weighted_average_score', 'total_score', 'overall_score'])]
        key_fields['total_score'] = total_score_fields[0] if total_score_fields else None
        print(f"总分字段: {key_fields['total_score']}")

        # 寻找三大支柱分数
        pillar_fields = {
            'environmental': [col for col in available_columns if 'environmental_pillar_score' in col.lower()],
            'social': [col for col in available_columns if 'social_pillar_score' in col.lower()],
            'governance': [col for col in available_columns if 'governance_pillar_score' in col.lower()]
        }

        for pillar, fields in pillar_fields.items():
            key_fields[f'{pillar}_score'] = fields[0] if fields else None
            print(f" {pillar.capitalize()}支柱分数: {key_fields[f'{pillar}_score']}")

        return key_fields

    def prepare_esg_data(self, key_fields):
        
        print("\n" + "=" * 80)
        print("3. 准备ESG数据")
        print("=" * 80)

        if self.financial_data is None:
            print("❌ 没有可用的数据")
            return False

        # 创建数据副本
        analysis_data = self.financial_data.copy()

        # 处理日期字段
        if key_fields['date']:
            try:
                analysis_data['year'] = pd.to_datetime(analysis_data[key_fields['date']]).dt.year
                print(f"✅ 已提取年份信息: {analysis_data['year'].min()} - {analysis_data['year'].max()}")
            except Exception as e:
                print(f"⚠️ 日期字段处理失败: {e}")
                # 创建模拟年份
                analysis_data['year'] = 2023
                print("⚠️ 使用默认年份2023")

        # 重命名字段以便统一使用
        field_mapping = {}
        if key_fields['name']:
            field_mapping[key_fields['name']] = 'company_name'
        if key_fields['rating']:
            field_mapping[key_fields['rating']] = 'esg_rating'
        if key_fields['industry']:
            field_mapping[key_fields['industry']] = 'industry'
        if key_fields['total_score']:
            field_mapping[key_fields['total_score']] = 'total_esg_score'
        if key_fields.get('environmental_score'):
            field_mapping[key_fields['environmental_score']] = 'environmental_score'
        if key_fields.get('social_score'):
            field_mapping[key_fields['social_score']] = 'social_score'
        if key_fields.get('governance_score'):
            field_mapping[key_fields['governance_score']] = 'governance_score'

        analysis_data = analysis_data.rename(columns=field_mapping)
        print(f"✅ 字段重命名完成: {field_mapping}")

        # 更新financial_data
        self.financial_data = analysis_data
        return True
        
    def calculate_esg_metrics(self):
        """计算ESG指标"""
        print("\n" + "=" * 80)
        print("4. 计算ESG指标")
        print("=" * 80)
        
        if self.financial_data is None or self.financial_data.empty:
            print("❌ 没有可用的ESG数据")
            return
      
        metrics_calculated = []

        # 检查并处理ESG分数
        score_columns = ['total_esg_score', 'environmental_score', 'social_score', 'governance_score']
        available_scores = [col for col in score_columns if col in self.financial_data.columns]

        if available_scores:
            print(f"✅ 可用的ESG分数字段: {available_scores}")
            metrics_calculated.extend(available_scores)

        # 如果有多个分数，计算平均分和总分
        if len(available_scores) >= 3:
            try:
                # 计算三大支柱平均分
                self.financial_data['esg_pillar_avg'] = self.financial_data[available_scores].mean(axis=1).round(2)
                metrics_calculated.append('三大支柱平均分')
                print("✅ 计算三大支柱平均分完成")
            except:
                print("⚠️ 计算三大支柱平均分失败")

        # 评级分布分析
        if 'esg_rating' in self.financial_data.columns:
            rating_counts = self.financial_data['esg_rating'].value_counts()
            print(f"\n📊 ESG评级分布:")
            for rating, count in rating_counts.items():
                print(f"  - {rating}: {count} 家公司")
        
        if metrics_calculated:
            print(f"\n📊 成功分析 {len(metrics_calculated)} 个ESG指标")

            # 显示计算结果预览
            display_cols = ['company_name', 'year'] if 'company_name' in self.financial_data.columns else ['year']
            display_cols.extend(available_scores[:3])  # 只显示前3个分数

            print("\nESG指标预览:")
            print(self.financial_data[display_cols].head(10).to_string(index=False))
        else:
            print("⚠️ 未能计算任何ESG指标")
   
    def descriptive_analysis(self):
        """描述性统计分析"""
        print("\n" + "=" * 80)
        print("5. 描述性统计分析")
        print("=" * 80)
          
        if self.financial_data is None or self.financial_data.empty:
            print("❌ 没有可用的ESG数据")
            return

        # 数值字段统计
        numeric_cols = self.financial_data.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            print("📈 数值字段描述统计:")
            # 只显示前10个数值字段的统计信息
            display_cols = numeric_cols[:10] if len(numeric_cols) > 10 else numeric_cols
            print(self.financial_data[display_cols].describe().round(2))

        # 按行业统计（如果有行业信息）
        if 'industry' in self.financial_data.columns and 'total_esg_score' in self.financial_data.columns:
            industry_stats = self.financial_data.groupby('industry').agg({
                'total_esg_score': ['count', 'mean', 'std', 'min', 'max']
            }).round(2)

            print("\n🏭 各行业ESG评分统计:")
            print(industry_stats)

        # 评级统计
        if 'esg_rating' in self.financial_data.columns:
            rating_stats = self.financial_data['esg_rating'].describe()
            print(f"\n⭐ ESG评级统计:")
            print(f"  唯一评级数量: {rating_stats['unique']}")
            print(f"  最常见评级: {rating_stats['top']} (出现{rating_stats['freq']}次)")

    def create_visualizations(self):
        """创建ESG数据可视化图表"""
        print("\n" + "=" * 80)
        print("6. 创建ESG数据可视化分析")
        print("=" * 80)

        if self.financial_data is None or self.financial_data.empty:
            print("❌ 没有可用的ESG数据")
            return

        # 创建图表 - 使用更大的图像尺寸和更多的间距
        fig = plt.figure(figsize=(18, 16), dpi=150)  # 进一步增大图像尺寸
        fig.suptitle('ESG数据分析可视化', fontsize=18, fontweight='bold', y=0.98)

        # 使用GridSpec进行更精细的布局控制 - 增加行间距
        gs = fig.add_gridspec(2, 2, hspace=0.5, wspace=0.3)  # 增加hspace从0.3到0.5

        axes = [
            fig.add_subplot(gs[0, 0]),
            fig.add_subplot(gs[0, 1]),
            fig.add_subplot(gs[1, 0]),
            fig.add_subplot(gs[1, 1])
        ]

        # 子图1: ESG总分分布
        if 'total_esg_score' in self.financial_data.columns:
            data = self.financial_data['total_esg_score'].dropna()
            if len(data) > 0:
                axes[0].hist(data, bins=20, alpha=0.7, color='skyblue',
                             edgecolor='black', linewidth=0.5)
                axes[0].set_title('ESG总分分布', fontweight='bold', pad=20)  # 增加标题间距
                axes[0].set_xlabel('ESG总分', labelpad=15)  # 增加标签间距
                axes[0].set_ylabel('公司数量', labelpad=15)
                axes[0].grid(True, alpha=0.3, linestyle='--')
                # 添加统计信息
                axes[0].text(0.05, 0.95, f'样本数: {len(data)}\n均值: {data.mean():.2f}',
                             transform=axes[0].transAxes, verticalalignment='top',
                             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5),
                             fontsize=10)

        # 子图2: ESG评级分布 - 优化x轴显示
        if 'esg_rating' in self.financial_data.columns:
            rating_counts = self.financial_data['esg_rating'].value_counts()
            if len(rating_counts) > 0:
                # 如果评级数量太多，只显示前10个
                if len(rating_counts) > 10:
                    rating_counts = rating_counts.head(10)
                    print(f"⚠️ 评级数量过多，只显示前10个最常见的评级")

                bars = axes[1].bar(range(len(rating_counts)), rating_counts.values,
                                   color='lightcoral', alpha=0.7, edgecolor='black', linewidth=0.5)
                axes[1].set_title('ESG评级分布', fontweight='bold', pad=20)
                axes[1].set_xlabel('ESG评级', labelpad=15)
                axes[1].set_ylabel('公司数量', labelpad=15)
                axes[1].set_xticks(range(len(rating_counts)))

                # 优化x轴标签显示
                labels = rating_counts.index
                # 如果标签太长，进行截断
                truncated_labels = [label[:8] + '...' if len(str(label)) > 8 else str(label) for label in labels]

                axes[1].set_xticklabels(truncated_labels,
                                        rotation=45,
                                        ha='right',
                                        fontsize=9)  # 减小字体大小

                axes[1].grid(True, alpha=0.3, linestyle='--')

                # 在柱状图上添加数值标签
                for i, bar in enumerate(bars):
                    height = bar.get_height()
                    axes[1].text(bar.get_x() + bar.get_width() / 2., height,
                                 f'{int(height)}', ha='center', va='bottom', fontsize=8)

        # 子图3: 三大支柱分数对比（如果可用）
        pillar_scores = []
        pillar_labels = []
        for pillar in ['environmental_score', 'social_score', 'governance_score']:
            if pillar in self.financial_data.columns:
                valid_data = self.financial_data[pillar].dropna()
                if len(valid_data) > 0:
                    pillar_scores.append(valid_data.mean())
                    pillar_labels.append(pillar.replace('_score', '').capitalize())

        if len(pillar_scores) >= 2:
            colors = ['lightgreen', 'lightblue', 'gold']
            bars = axes[2].bar(range(len(pillar_scores)), pillar_scores,
                               color=colors[:len(pillar_scores)], alpha=0.7,
                               edgecolor='black', linewidth=0.5)
            axes[2].set_title('ESG三大支柱平均分对比', fontweight='bold', pad=20)
            axes[2].set_xlabel('ESG支柱', labelpad=15)
            axes[2].set_ylabel('平均分数', labelpad=15)
            axes[2].set_xticks(range(len(pillar_scores)))

            # 简化支柱标签
            simplified_labels = []
            for label in pillar_labels:
                if label == 'Environmental':
                    simplified_labels.append('环境(E)')
                elif label == 'Social':
                    simplified_labels.append('社会(S)')
                elif label == 'Governance':
                    simplified_labels.append('治理(G)')
                else:
                    simplified_labels.append(label)

            axes[2].set_xticklabels(simplified_labels, rotation=0, fontsize=11)  # 稍微增大字体
            axes[2].grid(True, alpha=0.3, linestyle='--')

            # 在柱状图上添加数值标签
            for i, bar in enumerate(bars):
                height = bar.get_height()
                axes[2].text(bar.get_x() + bar.get_width() / 2., height,
                             f'{height:.2f}', ha='center', va='bottom', fontsize=10)

        # 子图4: 行业ESG表现（如果有行业数据）
        if 'industry' in self.financial_data.columns and 'total_esg_score' in self.financial_data.columns:
            industry_avg = self.financial_data.groupby('industry')['total_esg_score'].mean().nlargest(8)
            if len(industry_avg) > 0:
                bars = axes[3].bar(range(len(industry_avg)), industry_avg.values,
                                   color='orange', alpha=0.7, edgecolor='black', linewidth=0.5)
                axes[3].set_title('各行业平均ESG评分', fontweight='bold', pad=20)
                axes[3].set_xlabel('行业', labelpad=15)
                axes[3].set_ylabel('平均ESG评分', labelpad=15)
                axes[3].set_xticks(range(len(industry_avg)))

                # 优化行业名称显示
                industry_labels = []
                for label in industry_avg.index:
                    if len(str(label)) > 12:
                        # 如果行业名称太长，进行截断
                        industry_labels.append(str(label)[:10] + '...')
                    else:
                        industry_labels.append(str(label))

                axes[3].set_xticklabels(industry_labels,
                                        rotation=45,
                                        ha='right',
                                        fontsize=9)  # 减小字体大小

                axes[3].grid(True, alpha=0.3, linestyle='--')

                # 在柱状图上添加数值标签
                for i, bar in enumerate(bars):
                    height = bar.get_height()
                    axes[3].text(bar.get_x() + bar.get_width() / 2., height,
                                 f'{height:.2f}', ha='center', va='bottom', fontsize=8)

        # 使用更宽松的布局
        plt.tight_layout(pad=4.0)  # 增加pad参数，从默认的1.08增加到4.0

        # 在显示前添加一些间距
        print("\n📈 正在生成ESG可视化图表...")
        print("⏳ 请稍候，图表正在渲染...")
        plt.show()

        # 图表显示后添加分隔
        print("\n" + "=" * 60)
        print("🎨 ESG可视化图表显示完成")
        print("=" * 60)

    def generate_summary_report(self):
        """生成ESG分析总结报告"""
        print("\n" + "=" * 80)
        print("ESG分析总结报告")
        print("=" * 80)

        if self.financial_data is None:
            print("❌ 没有可分析的数据")
            return

        print("📋 ESG分析总结:")
        print(f"• 分析数据量: {len(self.financial_data)} 条记录")

        if 'company_name' in self.financial_data.columns:
            print(f"• 涉及公司数量: {self.financial_data['company_name'].nunique()} 家")

        if 'year' in self.financial_data.columns:
            print(f"• 数据时间范围: {self.financial_data['year'].min()} - {self.financial_data['year'].max()}")

        if 'total_esg_score' in self.financial_data.columns:
            avg_score = self.financial_data['total_esg_score'].mean()
            print(f"• 平均ESG总分: {avg_score:.2f}")

        if 'esg_rating' in self.financial_data.columns:
            top_rating = self.financial_data['esg_rating'].mode().iloc[0] if not self.financial_data[
                'esg_rating'].empty else 'N/A'
            print(f"• 最常见ESG评级: {top_rating}")

        if 'industry' in self.financial_data.columns:
            print(f"• 涉及行业数量: {self.financial_data['industry'].nunique()} 个")

        print("\n💡 ESG数据分析建议:")
        print("1. 关注ESG三大支柱的平衡发展")
        print("2. 分析不同行业的ESG表现差异")
        print("3. 跟踪ESG评级的动态变化")
        print("4. 识别ESG表现优异的公司和行业")

    def run_complete_analysis(self):
        """运行完整的ESG分析流程"""
        print("🚀 开始ESG数据分析（本地文件版）")
        print("=" * 80)

        # 加载本地数据
        if not self.load_local_data():
            print("❌ 无法加载数据文件，分析终止")
            return

        try:
            # 执行分析步骤 - 添加步骤间分隔
            print("\n" + "🔍 步骤1: 探索ESG数据字段结构")
            self.explore_data_fields()

            print("\n" + "🔑 步骤2: 识别关键ESG字段")
            key_fields = self.identify_key_fields()

            print("\n" + "🛠️ 步骤3: 准备ESG数据")
            if self.prepare_esg_data(key_fields):
                print("\n" + "📈 步骤4: 计算ESG指标")
                self.calculate_esg_metrics()

                print("\n" + "📊 步骤5: 描述性统计分析")
                self.descriptive_analysis()

                print("\n" + "🎨 步骤6: 创建可视化图表")
                self.create_visualizations()

                print("\n" + "📋 步骤7: 生成总结报告")
                self.generate_summary_report()
            else:
                print("❌ 数据准备失败，无法继续分析")

        except Exception as e:
            print(f"❌ 分析过程中出现错误: {e}")
            import traceback
            traceback.print_exc()

        finally:
            print("\n" + "=" * 50)
            print("✅ ESG分析完成！")
            print("=" * 50)


# 主程序入口
if __name__ == "__main__":
    print("ESG数据分析工具 - 本地文件版")
    print("=" * 50)

    # 可以指定不同的文件路径
    file_path = 'znttaqleyuk9pjxj.csv'  # 默认文件路径

    # 创建分析器实例
    analyzer = ESGDataAnalyzer(file_path)

    # 运行完整分析
    analyzer.run_complete_analysis()
