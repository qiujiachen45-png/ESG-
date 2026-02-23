import matplotlib.pyplot as plt

# 数据（时间升序）
months = ['2022-12', '2023-01', '2023-02', '2023-03', '2023-04', '2023-06']
values = [16, 34, 22, 20, 27, 45]

# 绘图
plt.figure(figsize=(8,5))
bars = plt.bar(months, values, color='lightcoral', alpha=0.7)

# 在每根柱子上方添加数值标签
for bar, value in zip(bars, values):
    plt.text(bar.get_x() + bar.get_width()/2, value + 0.5, str(value),
             ha='center', va='bottom', fontsize=10)

# 坐标轴与标题
plt.xlabel('日期', fontsize=12)
plt.ylabel('月度投诉量', fontsize=12)
plt.title('按时间顺序排列的投诉量变化', fontsize=13)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
