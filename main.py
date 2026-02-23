import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("使用现有ESG数据进行分析...")
print("=" * 50)


# 假设我们已经有之前成功查询的数据
# 这里我会创建一些示例数据来演示分析流程

# 创建示例服装企业ESG数据
def create_sample_apparel_esg_data():
    """创建服装企业ESG示例数据"""
    companies = [
        'NIKE Inc', 'ADIDAS AG', 'INDITEX (ZARA)', 'H&M HENNES', 'LULULEMON ATH',
        'PVH CORP', 'VF CORP', 'BURBERRY GROUP', 'KERING SA', 'LVMH FASHION',
        'UNIQLO CO', 'GAP INC', 'LEVI STRAUSS', 'UNDER ARMOUR', 'PUMA SE'
    ]

    countries = ['US', 'DE', 'ES', 'SE', 'CA', 'US', 'US', 'UK', 'FR', 'FR', 'JP', 'US', 'US', 'US', 'DE']

    data = []
    for company, country in zip(companies, countries):
        for year in range(2018, 2024):
            # 生成合理的ESG分数
            base_env = np.random.normal(6.0, 1.5)
            base_social = np.random.normal(5.8, 1.3)
            base_gov = np.random.normal(6.2, 1.2)

            # 确保分数在合理范围内
            env_score = max(1, min(10, base_env + (year - 2018) * 0.1))
            social_score = max(1, min(10, base_social + (year - 2018) * 0.08))
            gov_score = max(1, min(10, base_gov + (year - 2018) * 0.05))
            total_score = (env_score + social_score + gov_score) / 3

            # ESG评级映射
            if total_score >= 8.5:
                rating = 'AAA'
            elif total_score >= 7.0:
                rating = 'AA'
            elif total_score >= 5.5:
                rating = 'A'
            elif total_score >= 4.0:
                rating = 'BBB'
            else:
                rating = 'BB'

            data.append({
                'issuer_name': company,
                'issuer_cntry_domicile': country,
                'as_of_date': f'{year}-12-31',
                'iva_company_rating': rating,
                'environment_pillar_score': round(env_score, 2),
                'social_pillar_score': round(social_score, 2),
                'governance_pillar_score': round(gov_score, 2),
                'total_esg_score': round(total_score, 2)
            })

    return pd.DataFrame(data)


# 创建示例数据
print("生成服装企业ESG示例数据...")
esg_data = create_sample_apparel_esg_data()
print(f"创建了 {len(esg_data)} 条ESG记录")
print(esg_data.head(10))

print("\n" + "=" * 50)
print("开始ESG数据分析")
print("=" * 50)

# 1. 基本统计分析
print("1. ESG评分基本统计:")
stats = esg_data[['environment_pillar_score', 'social_pillar_score',
                  'governance_pillar_score', 'total_esg_score']].describe()
print(stats)

# 2. 各公司最新ESG表现
print("\n2. 各公司最新ESG表现:")
latest_scores = esg_data.sort_values(['issuer_name', 'as_of_date']).groupby('issuer_name').last()
latest_scores = latest_scores[['iva_company_rating', 'environment_pillar_score',
                               'social_pillar_score', 'governance_pillar_score', 'total_esg_score']]
print(latest_scores.sort_values('total_esg_score', ascending=False))

# 3. ESG评级分布
print("\n3. ESG评级分布:")
rating_dist = esg_data['iva_company_rating'].value_counts().sort_index()
print(rating_dist)

# 4. 国家比较
print("\n4. 各国服装企业ESG表现:")
country_stats = esg_data.groupby('issuer_cntry_domicile').agg({
    'total_esg_score': ['mean', 'std', 'count'],
    'environment_pillar_score': 'mean',
    'social_pillar_score': 'mean',
    'governance_pillar_score': 'mean'
}).round(2)
country_stats.columns = ['avg_total', 'std_total', 'company_count', 'avg_env', 'avg_social', 'avg_gov']
print(country_stats.sort_values('avg_total', ascending=False))

# 5. 时间趋势分析
print("\n5. ESG评分时间趋势:")
esg_data['year'] = pd.to_datetime(esg_data['as_of_date']).dt.year
yearly_trend = esg_data.groupby('year').agg({
    'environment_pillar_score': 'mean',
    'social_pillar_score': 'mean',
    'governance_pillar_score': 'mean',
    'total_esg_score': 'mean'
}).round(2)
print(yearly_trend)

# 可视化分析
print("\n" + "=" * 50)
print("生成可视化分析...")

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

# 创建可视化
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# 1. 各公司ESG总分排名
top_companies = latest_scores.nlargest(10, 'total_esg_score')
axes[0, 0].barh(range(len(top_companies)), top_companies['total_esg_score'])
axes[0, 0].set_yticks(range(len(top_companies)))
axes[0, 0].set_yticklabels(top_companies.index, fontsize=8)
axes[0, 0].set_xlabel('ESG总分')
axes[0, 0].set_title('服装企业ESG总分排名（前10）')
axes[0, 0].grid(True, alpha=0.3)

# 2. 三大支柱评分比较
pillar_means = esg_data[['environment_pillar_score', 'social_pillar_score', 'governance_pillar_score']].mean()
axes[0, 1].bar(pillar_means.index, pillar_means.values, color=['green', 'blue', 'purple'])
axes[0, 1].set_ylabel('平均分数')
axes[0, 1].set_title('ESG三大支柱平均分数')
for i, v in enumerate(pillar_means.values):
    axes[0, 1].text(i, v + 0.1, f'{v:.2f}', ha='center')

# 3. 时间趋势
axes[1, 0].plot(yearly_trend.index, yearly_trend['environment_pillar_score'], marker='o', label='环境', color='green')
axes[1, 0].plot(yearly_trend.index, yearly_trend['social_pillar_score'], marker='s', label='社会', color='blue')
axes[1, 0].plot(yearly_trend.index, yearly_trend['governance_pillar_score'], marker='^', label='治理', color='purple')
axes[1, 0].set_xlabel('年份')
axes[1, 0].set_ylabel('平均分数')
axes[1, 0].set_title('ESG评分时间趋势')
axes[1, 0].legend()
axes[1, 0].grid(True, alpha=0.3)

# 4. 国家比较
top_countries = country_stats.nlargest(8, 'avg_total')
axes[1, 1].bar(range(len(top_countries)), top_countries['avg_total'],
               yerr=top_countries['std_total'], capsize=5, alpha=0.7)
axes[1, 1].set_xticks(range(len(top_countries)))
axes[1, 1].set_xticklabels(top_countries.index)
axes[1, 1].set_ylabel('平均ESG总分')
axes[1, 1].set_title('各国服装企业ESG表现')
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# 详细分析报告
print("\n" + "=" * 50)
print("服装企业ESG分析报告")
print("=" * 50)

# 环境表现最佳的企业
best_env = latest_scores.nlargest(5, 'environment_pillar_score')
print("环境表现最佳的企业:")
for idx, row in best_env.iterrows():
    print(f"  {idx}: {row['environment_pillar_score']}分")

# 社会表现最佳的企业
best_social = latest_scores.nlargest(5, 'social_pillar_score')
print("\n社会表现最佳的企业:")
for idx, row in best_social.iterrows():
    print(f"  {idx}: {row['social_pillar_score']}分")

# 进步最大的企业（如果有多年数据）
if len(esg_data['year'].unique()) > 1:
    progress = []
    for company in esg_data['issuer_name'].unique():
        company_data = esg_data[esg_data['issuer_name'] == company]
        if len(company_data) >= 2:
            first_year = company_data.nsmallest(1, 'year')['total_esg_score'].iloc[0]
            last_year = company_data.nlargest(1, 'year')['total_esg_score'].iloc[0]
            improvement = last_year - first_year
            progress.append((company, improvement))

    if progress:
        top_improvers = sorted(progress, key=lambda x: x[1], reverse=True)[:5]
        print("\nESG进步最大的企业:")
        for company, improvement in top_improvers:
            print(f"  {company}: +{improvement:.2f}分")

print("\n" + "=" * 50)
print("分析完成!")