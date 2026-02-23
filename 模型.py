import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False


def create_simple_risk_system():
    """创建简明的风险预警体系图"""
    fig, ax = plt.subplots(figsize=(12, 8))

    # 设置背景
    ax.set_facecolor('#F0F8FF')

    # 1. 三大风险源
    risks = [
        {'name': '全球变暖', 'pos': (2, 7), 'color': '#FF9999', 'icon': '全球变暖'},
        {'name': '极端天气', 'pos': (6, 7), 'color': '#99CCFF', 'icon': '极端天气'},
        {'name': '地缘政治', 'pos': (10, 7), 'color': '#99FF99', 'icon':'地缘政治'}
    ]

    for risk in risks:
        x, y = risk['pos']
        # 风险图标
        ax.text(x, y + 0.3, risk['icon'], fontsize=20, ha='center', va='center')
        # 风险名称
        ax.text(x, y, risk['name'], fontsize=12, fontweight='bold',
                ha='center', va='center',
                bbox=dict(boxstyle="round,pad=0.3", facecolor=risk['color'], alpha=0.7))
        # 连接到预警中心
        ax.annotate('', xy=(6, 4), xytext=(x, y - 0.2),
                    arrowprops=dict(arrowstyle='->', color='gray', lw=1.5, alpha=0.6))

    # 2. 预警中心
    ax.add_patch(plt.Circle((6, 4), 0.8, color='#FF6B6B', alpha=0.9))
    ax.text(6, 4, '风险预警\n中心', fontsize=11, fontweight='bold',
            ha='center', va='center', color='white')

    # 3. 输出结果
    outputs = [
        {'name': '供应链重构', 'pos': (3, 1), 'color': '#FFCC00', 'icon': '重构'},
        {'name': '价格波动', 'pos': (6, 1), 'color': '#CC99FF', 'icon': '波动'},
        {'name': '风险预警', 'pos': (9, 1), 'color': '#66CCCC', 'icon': '报警'}
    ]

    for output in outputs:
        x, y = output['pos']
        # 输出图标
        ax.text(x, y - 0.3, output['icon'], fontsize=18, ha='center', va='center')
        # 输出名称
        ax.text(x, y, output['name'], fontsize=11, fontweight='bold',
                ha='center', va='center',
                bbox=dict(boxstyle="round,pad=0.3", facecolor=output['color'], alpha=0.7))
        # 从预警中心连接
        ax.annotate('', xy=(x, y + 0.3), xytext=(6, 3.2),
                    arrowprops=dict(arrowstyle='->', color='gray', lw=1.5, alpha=0.6))

    # 4. 核心模型
    ax.text(6, 5.5, '数学模型: R = f(气候, 天气, 政治)', fontsize=10,
            ha='center', va='center', style='italic',
            bbox=dict(boxstyle="round,pad=0.3", facecolor='lightgray', alpha=0.8))

    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.set_title('供应链风险预警体系', fontsize=16, fontweight='bold', pad=20)
    ax.axis('off')

    plt.tight_layout()
    plt.savefig('简明风险预警体系.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.show()


# 运行程序
create_simple_risk_system()