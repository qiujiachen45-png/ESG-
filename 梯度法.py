import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import quad


# 定义函数
def f(x):
    return np.sin(x)


# 区间
a, b = 0, np.pi
true_val, _ = quad(f, a, b)

# 初始化图形
fig, ax = plt.subplots(figsize=(8, 5))
x = np.linspace(a, b, 400)
ax.plot(x, f(x), 'r', label='f(x)=sin(x)')
ax.fill_between(x, 0, f(x), alpha=0.1, color='r')
ax.set_xlim(a, b)
ax.set_ylim(0, 1.1)
ax.legend()
ax.set_title("Trapezoidal Rule Approximation")

# 存储梯形区域的 PolyCollection
traps = []


# 更新函数
def update(n):
    # 删除上一帧的梯形
    for trap in traps:
        trap.remove()
    traps.clear()

    N = n + 1  # 梯形数量
    xs = np.linspace(a, b, N + 1)
    ys = f(xs)
    h = (b - a) / N
    trap_sum = h * (np.sum(ys) - 0.5 * (ys[0] + ys[-1]))

    # 绘制每个梯形
    for i in range(N):
        trap = ax.fill_between([xs[i], xs[i + 1]], [f(xs[i]), f(xs[i + 1])],
                               color='skyblue', alpha=0.5)
        traps.append(trap)

    ax.set_title(f"n={N}  Trapezoidal ≈ {trap_sum:.6f},  True = {true_val:.6f}, Error = {abs(true_val - trap_sum):.6f}")
    return traps


# 创建动画
ani = FuncAnimation(fig, update, frames=range(2, 50), interval=300, repeat=False)

plt.show()
