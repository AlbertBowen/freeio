import matplotlib.pyplot as plt

# 数据
categories = ['A', 'B', 'C', 'D', 'E']
values = [100, 200, 1500, 400, 300]

# 创建图形和子图对象
fig, ax = plt.subplots()

# 绘制完整的柱状图
ax.bar(categories, values)

# 设置断轴的范围
break_range = (500, 1500)  # 定义断轴的范围
ax.set_ylim(0, break_range[0])  # 设置上半部分的y轴范围
ax.spines['bottom'].set_visible(False)  # 隐藏底部轴线

# 绘制断开的部分
ax.spines['top'].set_visible(False)  # 隐藏顶部轴线
ax.spines['bottom'].set_visible(True)  # 显示底部轴线
ax.spines['bottom'].set_position(('outward', 10))  # 将底部轴线放置在上半部分的下方
ax.set_ylim(break_range[1], max(values))  # 设置下半部分的y轴范围

# 添加断轴标记
ax.plot([0, len(categories)], [break_range[0], break_range[0]], color='red', linewidth=1)  # 上半部分的断轴线
ax.plot([0, len(categories)], [break_range[1], break_range[1]], color='red', linewidth=1)  # 下半部分的断轴线
ax.annotate('...', xy=(len(categories) - 0.5, break_range[0]), xytext=(len(categories) - 0.5, break_range[0] - 200),
            ha='center', va='top', arrowprops=dict(arrowstyle='-', lw=1))  # 上半部分的断轴省略号
ax.annotate('...', xy=(len(categories) - 0.5, break_range[1]), xytext=(len(categories) - 0.5, break_range[1] + 200),
            ha='center', va='bottom', arrowprops=dict(arrowstyle='-', lw=1))  # 下半部分的断轴省略号

# 显示图形
plt.show()