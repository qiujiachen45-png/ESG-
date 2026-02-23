import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 下载并指定中文字体文件
# 可以从 https://fonts.google.com/noto/specimen/Noto+Sans+SC 下载Noto Sans SC字体
font_path = 'NotoSansSC-Regular.ttf'  # 替换为您的字体文件路径

if os.path.exists(font_path):
    prop = fm.FontProperties(fname=font_path)
    plt.rcParams['font.family'] = prop.get_name()
else:
    print("字体文件未找到，使用默认字体")

# 其余代码与方案一相同

# 设置中文字体和样式，确保在PPT中显示清晰
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']  # 兼容性更好的中文字体
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('seaborn-v0_8')  # 使用更现代的seaborn样式

# 核心数据
years = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
salary = [51483, 56360, 62029, 67569, 74318, 82461, 90501, 97379, 106837, 114029]

# 创建图表
fig, ax = plt.subplots(figsize=(14, 8))  # 适合PPT的宽屏比例

# 绘制组合图表：柱状图 + 趋势线
bars = ax.bar(years, salary, color='#1f77b4', alpha=0.7, width=0.6, label='年平均工资')
line = ax.plot(years, salary, 'ro-', linewidth=4, markersize=10, markerfacecolor='red',
               markeredgecolor='darkred', markeredgewidth=2, label='增长趋势')

# 设置标题和标签
ax.set_title('中国城镇非私营单位就业人员年平均工资\n(2013-2022)',
             fontsize=20, fontweight='bold', pad=25)
ax.set_xlabel('年份', fontsize=14, fontweight='bold', labelpad=10)
ax.set_ylabel('年平均工资（元）', fontsize=14, fontweight='bold', labelpad=10)

# 在柱子上方显示数值（以"万"为单位）
for i, v in enumerate(salary):
    ax.text(years[i], v + 4000, f'{v/10000:.1f}万',
            ha='center', va='bottom', fontsize=11, fontweight='bold')

# 设置坐标轴样式
ax.tick_params(axis='both', which='major', labelsize=12)
ax.set_ylim(0, 130000)  # 为顶部标签留出空间

# 添加网格线
ax.grid(True, alpha=0.3, axis='y')

# 在图表内部添加关键结论
growth_rate = ((salary[-1] - salary[0]) / salary[0]) * 100
textstr = f'核心趋势：十年增长{growth_rate:.0f}%，实现翻番'
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=16,
        fontweight='bold', color='red', verticalalignment='top',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.3))

# 添加图例
ax.legend(loc='upper left', fontsize=12, framealpha=0.9)

# 优化布局
plt.tight_layout()

# 保存为高清图片（便于插入PPT）
plt.savefig('劳动力成本趋势图.png', dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none')

# 显示图表
plt.show()

# 打印核心数据点
print("核心数据摘要：")
print(f"• 2013年：{salary[0]:,} 元")
print(f"• 2022年：{salary[-1]:,} 元")
print(f"• 绝对增长：{salary[-1]-salary[0]:,} 元")
print(f"• 增长率：{growth_rate:.1f}%")