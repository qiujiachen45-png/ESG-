

在ESG分析大赛中数据非常重要，本组通过Wharton获取近近几年公司的数据进行全方位分析，最终形成分析报告

<img width="1282" height="712" alt="image" src="https://github.com/user-attachments/assets/d084b7cc-cd4f-4767-9ec8-9be09bcd18f3" />
<img width="1302" height="735" alt="image" src="https://github.com/user-attachments/assets/2fa037a1-c871-4be9-94b8-c40f86b8b757" />

一下为代码分析结果


🔍 步骤1: 探索ESG数据字段结构

================================================================================
1. 探索ESG数据字段结构
================================================================================
📊 共有 249 个字段
📈 数据记录数: 862

🏷️ 基础信息字段 (13个):
  - ASSESSMENT_CHANGE_DATE
  - AS_OF_DATE
  - COUNTRY_OF_INCORPORATION
  - INDUSTRY_ADJUSTED_SCORE
  - IND_INDUSTRY_EXPERTS
  - ISSUERID
  - ISSUER_CNTRY_DOMICILE
  - ISSUER_NAME
  - IVA_COMPANY_RATING
  - IVA_INDUSTRY
  - IVA_PREVIOUS_RATING
  - IVA_RATING_DATE
  - IVA_RATING_TREND

🌱 环境(E)相关字段 (40个):
  - BIODIV_LAND_USE_EXP_SCORE
  - BIODIV_LAND_USE_MGMT_SCORE
  - BIODIV_LAND_USE_SCORE
  - BIODIV_LAND_USE_WEIGHT
  - CARBON_EMISSIONS_EXP_SCORE
  - CARBON_EMISSIONS_MGMT_SCORE
  - CARBON_EMISSIONS_SCORE
  - CARBON_EMISSIONS_WEIGHT
  - CLIMATE_CHANGE_THEME_SCORE
  - CLIMATE_CHANGE_THEME_WEIGHT
  - ENERGY_EFFICIENCY_EXP_SCORE
  - ENERGY_EFFICIENCY_MGMT_SCORE
  - ENERGY_EFFICIENCY_SCORE
  - ENERGY_EFFICIENCY_WEIGHT
  - ENVIRONMENTAL_OPPS_THEME_SCORE

👥 社会(S)相关字段 (32个):
  - CHEM_SAFETY_EXP_SCORE
  - CHEM_SAFETY_MGMT_SCORE
  - CHEM_SAFETY_SCORE
  - CHEM_SAFETY_WEIGHT
  - FIN_PROD_SAFETY_EXP_SCORE
  - FIN_PROD_SAFETY_MGMT_SCORE
  - FIN_PROD_SAFETY_SCORE
  - FIN_PROD_SAFETY_WEIGHT
  - HLTH_SAFETY_EXP_SCORE
  - HLTH_SAFETY_MGMT_SCORE
  - HLTH_SAFETY_SCORE
  - HLTH_SAFETY_WEIGHT
  - HUMAN_CAPITAL_DEV_EXP_SCORE
  - HUMAN_CAPITAL_DEV_MGMT_SCORE
  - HUMAN_CAPITAL_DEV_SCORE

🏛️ 治理(G)相关字段 (49个):
  - AUDITOR_SINCE
  - AUDITS_COMP_BY_CURRENT_AUDITOR
  - AUDIT_COMMITTEE_MEETINGS_HELD
  - AVG_DIRECTOR_TENURE
  - AVG_IND_DIRECTOR_TENURE
  - BOARD_GOV_PILLAR_SD
  - BOARD_IND_MGMT_OTHER_PCT
  - BOARD_IND_OTHER_INT_PCT
  - BOARD_MAJORITY_IND_OF_OTHER_INT
  - BOARD_MAJORITY_IND_OTHER_INT_SD
  - BOARD_MEETINGS_HELD
  - BOARD_PCTL_GLOBAL
  - BOARD_PCTL_HOME
  - BOARD_REELECTION_FREQUENCY
  - BUSINESS_ETHICS_THEME_SCORE

⭐ 评分字段 (118个):
  - ACCESS_TO_COMM_EXP_SCORE
  - ACCESS_TO_COMM_MGMT_SCORE
  - ACCESS_TO_COMM_SCORE
  - ACCESS_TO_FIN_EXP_SCORE
  - ACCESS_TO_FIN_MGMT_SCORE
  - ACCESS_TO_FIN_SCORE
  - ACCESS_TO_HLTHCRE_EXP_SCORE
  - ACCESS_TO_HLTHCRE_MGMT_SCORE
  - ACCESS_TO_HLTHCRE_SCORE
  - ANTICOMP_PRACT_MGMT_SCORE
  - ANTICOMP_PRACT_SCORE
  - BIODIV_LAND_USE_EXP_SCORE
  - BIODIV_LAND_USE_MGMT_SCORE
  - BIODIV_LAND_USE_SCORE
  - BUSINESS_ETHICS_THEME_SCORE
  - BUS_ETHICS_FRAUD_MGMT_SCORE
  - BUS_ETHICS_FRAUD_SCORE
  - CARBON_EMISSIONS_EXP_SCORE
  - CARBON_EMISSIONS_MGMT_SCORE
  - CARBON_EMISSIONS_SCORE

🔑 步骤2: 识别关键ESG字段

================================================================================
2. 识别关键ESG字段
================================================================================
🏢 公司名称字段: ISSUER_NAME
📅 日期字段: AS_OF_DATE
⭐ 评级字段: IVA_RATING_DATE
🏭 行业字段: IVA_INDUSTRY
📊 总分字段: WEIGHTED_AVERAGE_SCORE
🌱 Environmental支柱分数: ENVIRONMENTAL_PILLAR_SCORE
🌱 Social支柱分数: SOCIAL_PILLAR_SCORE
🌱 Governance支柱分数: GOVERNANCE_PILLAR_SCORE

🛠️ 步骤3: 准备ESG数据

================================================================================
3. 准备ESG数据
================================================================================
✅ 已提取年份信息: 2023 - 2024
✅ 字段重命名完成: {'ISSUER_NAME': 'company_name', 'IVA_RATING_DATE': 'esg_rating', 'IVA_INDUSTRY': 'industry', 'WEIGHTED_AVERAGE_SCORE': 'total_esg_score', 'ENVIRONMENTAL_PILLAR_SCORE': 'environmental_score', 'SOCIAL_PILLAR_SCORE': 'social_score', 'GOVERNANCE_PILLAR_SCORE': 'governance_score'}

📈 步骤4: 计算ESG指标

================================================================================
4. 计算ESG指标
================================================================================
✅ 可用的ESG分数字段: ['total_esg_score', 'environmental_score', 'social_score', 'governance_score']
✅ 计算三大支柱平均分完成

📊 ESG评级分布:
  - 2023-06-28: 45 家公司
  - 2023-01-27: 34 家公司
  - 2023-06-27: 27 家公司
  - 2023-04-06: 22 家公司
  - 2022-12-20: 22 家公司
  - 2023-05-26: 20 家公司
  - 2023-05-09: 20 家公司
  - 2021-03-19: 19 家公司
  - 2023-06-23: 18 家公司
  - 2022-12-23: 16 家公司
  - 2022-10-26: 14 家公司
  - 2023-08-22: 14 家公司
  - 2023-08-29: 14 家公司
  - 2022-11-28: 13 家公司
  - 2022-09-12: 13 家公司
  - 2022-12-16: 13 家公司
  - 2022-09-15: 13 家公司
  - 2022-12-05: 13 家公司
  - 2023-02-10: 12 家公司
  - 2023-01-09: 12 家公司
  - 2023-02-24: 12 家公司
  - 2023-03-29: 12 家公司
  - 2023-02-14: 12 家公司
  - 2023-03-03: 12 家公司
  - 2023-09-27: 12 家公司
  - 2022-11-23: 12 家公司
  - 2022-11-14: 12 家公司
  - 2023-02-22: 12 家公司
  - 2023-04-18: 11 家公司
  - 2023-03-27: 11 家公司
  - 2023-04-26: 11 家公司
  - 2023-04-11: 11 家公司
  - 2023-01-20: 11 家公司
  - 2023-04-25: 11 家公司
  - 2023-02-23: 10 家公司
  - 2022-09-28: 10 家公司
  - 2022-09-22: 10 家公司
  - 2022-09-23: 10 家公司
  - 2023-05-19: 10 家公司
  - 2023-05-24: 10 家公司
  - 2022-08-25: 10 家公司
  - 2022-12-21: 10 家公司
  - 2023-05-29: 10 家公司
  - 2022-11-24: 9 家公司
  - 2022-11-25: 9 家公司
  - 2022-07-28: 9 家公司
  - 2022-10-20: 8 家公司
  - 2023-07-27: 8 家公司
  - 2023-11-28: 8 家公司
  - 2022-05-26: 8 家公司
  - 2023-07-25: 8 家公司
  - 2023-07-21: 8 家公司
  - 2023-08-25: 7 家公司
  - 2022-06-27: 7 家公司
  - 2023-08-16: 7 家公司
  - 2023-08-28: 7 家公司
  - 2022-10-13: 7 家公司
  - 2022-08-28: 7 家公司
  - 2023-09-08: 6 家公司
  - 2023-09-26: 6 家公司
  - 2022-06-16: 6 家公司
  - 2023-12-21: 6 家公司
  - 2022-08-18: 6 家公司
  - 2023-09-22: 6 家公司
  - 2022-08-29: 6 家公司
  - 2023-09-12: 6 家公司
  - 2022-05-19: 5 家公司
  - 2023-10-25: 5 家公司
  - 2022-11-16: 5 家公司
  - 2023-11-17: 4 家公司
  - 2022-06-28: 4 家公司
  - 2022-01-20: 4 家公司
  - 2023-12-20: 3 家公司
  - 2021-10-08: 3 家公司
  - 2023-12-13: 3 家公司
  - 2023-12-11: 3 家公司
  - 2023-12-19: 3 家公司
  - 2022-03-04: 3 家公司
  - 2023-10-27: 3 家公司
  - 2024-02-16: 2 家公司
  - 2022-06-10: 2 家公司
  - 2024-01-16: 2 家公司
  - 2022-03-29: 2 家公司
  - 2024-01-23: 2 家公司
  - 2024-02-27: 2 家公司
  - 2024-01-29: 2 家公司
  - 2022-07-22: 2 家公司
  - 2022-02-03: 2 家公司
  - 2022-06-24: 1 家公司
  - 2022-03-17: 1 家公司
  - 2024-02-26: 1 家公司
  - 2024-02-23: 1 家公司
  - 2024-02-09: 1 家公司

📊 成功分析 5 个ESG指标

ESG指标预览:
           company_name  year  total_esg_score  environmental_score  social_score
CINEMARK HOLDINGS, INC.  2023             4.90                  8.3          0.05
CINEMARK HOLDINGS, INC.  2023             0.05                  8.3          0.05
CINEMARK HOLDINGS, INC.  2023             0.05                  8.3          0.05
CINEMARK HOLDINGS, INC.  2023             0.05                  8.3          0.05
CINEMARK HOLDINGS, INC.  2023             0.05                  8.3          0.05
CINEMARK HOLDINGS, INC.  2023             0.05                  8.3          0.05
CINEMARK HOLDINGS, INC.  2023             0.05                  8.3          0.05
CINEMARK HOLDINGS, INC.  2023             0.05                  8.3          0.05
CINEMARK HOLDINGS, INC.  2023             0.05                  8.3          0.05
CINEMARK HOLDINGS, INC.  2023             0.05                  8.3          0.05

📊 步骤5: 描述性统计分析

================================================================================
5. 描述性统计分析
================================================================================
📈 数值字段描述统计:
       IVA_RATING_TREND  ...  CLIMATE_CHANGE_THEME_SCORE
count            848.00  ...                      862.00
mean               0.20  ...                        4.24
std                0.58  ...                        3.39
min               -1.00  ...                        0.00
25%                0.00  ...                        0.10
50%                0.00  ...                        5.40
75%                1.00  ...                        7.05
max                2.00  ...                        9.90

[8 rows x 10 columns]

🏭 各行业ESG评分统计:
                                                   total_esg_score  ...     
                                                             count  ...  max
industry                                                            ...     
Asset Management & Custody Banks                                13  ...  7.1
Auto Components                                                 39  ...  5.3
Automobiles                                                     13  ...  5.6
Banks                                                           26  ...  5.9
Biotechnology                                                   11  ...  4.8
Building Products                                               13  ...  5.9
Casinos & Gaming                                                13  ...  6.5
Commercial Services & Supplies                                  13  ...  5.1
Construction & Engineering                                      13  ...  7.7
Construction & Farm Machinery & Heavy Trucks                    13  ...  5.5
Construction Materials                                          13  ...  5.5
Containers & Packaging                                          13  ...  5.8
Diversified Financials                                          39  ...  6.3
Electrical Equipment                                            13  ...  6.8
Electronic Equipment, Instruments & Components                  52  ...  5.4
Energy Equipment & Services                                     11  ...  6.3
Food Products                                                   26  ...  5.9
Health Care Equipment & Supplies                                26  ...  6.1
Health Care Providers & Services                                13  ...  6.6
Hotels & Travel                                                  6  ...  5.8
Industrial Machinery                                            26  ...  5.9
Life & Health Insurance                                         13  ...  4.8
Media & Entertainment                                           13  ...  5.3
Metals and Mining - Non-Precious Metals                         13  ...  5.2
Multi-Line Insurance & Brokerage                                13  ...  6.8
Oil & Gas Exploration & Production                              65  ...  5.6
Oil & Gas Refining, Marketing, Transportation &...              29  ...  6.4
Paper & Forest Products                                         26  ...  5.5
Pharmaceuticals                                                  2  ...  5.7
Real Estate Development & Diversified Activities                26  ...  6.9
Restaurants                                                     26  ...  4.8
Retail - Consumer Discretionary                                 13  ...  5.6
Road & Rail Transport                                           13  ...  5.2
Semiconductors & Semiconductor Equipment                        13  ...  6.2
Software & Services                                             26  ...  5.7
Specialty Chemicals                                             36  ...  5.8
Technology Hardware, Storage & Peripherals                      13  ...  4.7
Telecommunication Services                                      52  ...  7.3
Trading Companies & Distributors                                13  ...  6.9
Utilities                                                       52  ...  6.9

[40 rows x 5 columns]

⭐ ESG评级统计:
  唯一评级数量: 93
  最常见评级: 2023-06-28 (出现45次)

🎨 步骤6: 创建可视化图表

================================================================================
6. 创建ESG数据可视化分析
================================================================================
⚠️ 评级数量过多，只显示前10个最常见的评级

📈 正在生成ESG可视化图表...
⏳ 请稍候，图表正在渲染...

============================================================
🎨 ESG可视化图表显示完成
============================================================

📋 步骤7: 生成总结报告

================================================================================
ESG分析总结报告
================================================================================
📋 ESG分析总结:
• 分析数据量: 862 条记录
• 涉及公司数量: 70 家
• 数据时间范围: 2023 - 2024
• 平均ESG总分: 4.72
• 最常见ESG评级: 2023-06-28
• 涉及行业数量: 40 个

💡 ESG数据分析建议:
1. 关注ESG三大支柱的平衡发展
2. 分析不同行业的ESG表现差异
3. 跟踪ESG评级的动态变化
4. 识别ESG表现优异的公司和行业

==================================================
✅ ESG分析完成！
==================================================

进程已结束，退出代码为 0

<img width="3072" height="1515" alt="Figure_1111111ww1" src="https://github.com/user-attachments/assets/d95c5514-89be-4ae4-9d36-1b5d78a1f35a" />




