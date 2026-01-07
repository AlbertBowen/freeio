import matplotlib.pyplot as plt
import numpy as np
from matplotlib import gridspec


branch = 'eva_burst' # ['burst', 'distribution']
output = 'save' # ['show', 'save'] 


plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']  # 或者 'Nimbus Roman' / 'CMU Serif' 等 TrueType 字体
plt.rcParams['pdf.fonttype'] = 42  # 输出为 TrueType 字体，避免 Type3
plt.rcParams['ps.fonttype'] = 42



# 数据
time = np.linspace(0, 50, 50)  # 时间轴，从0到60秒
thpt_base = [41.005, 41.058, 41.047, 41.054, 40.329, 41.077, 41.065, 41.031, 41.057, 41.032, 36.078, 33.108, 31.066, 31.156, 30.235, 30.767, 31.425, 31.357, 30.837, 30.700, 27.684, 26.469, 26.674, 26.039, 26.251, 25.488, 24.004, 25.045, 24.363, 26.355, 24.144, 23.155, 22.779, 21.691, 21.952, 21.294, 21.145, 21.593, 20.998, 21.249, 18.564, 15.983, 16.012, 15.558, 16.566, 16.449, 15.291, 15.641, 15.155, 16.832]  # baseline (mpps)
thpt_shring = [64.803, 63.976, 64.898, 64.951, 63.923, 63.998, 64.969, 64.916, 64.977, 64.995] + [64.625, 56.164, 54.528, 55.326, 54.508, 55.503, 55.334, 54.221, 55.547, 56.212] + [47.798, 45.975, 44.707, 42.138, 42.732, 44.198, 42.592, 41.716, 43.767, 42.577] + [38.694, 35.024, 34.285, 36.743, 34.898, 34.003, 34.160, 34.252, 32.953, 33.051] + [27.271, 26.053, 21.799, 25.385, 24.688, 25.418, 25.456, 27.363, 23.535, 25.369]    # ShRing吞吐量 (mpps)
thpt_hostcc = [51.954, 52.964, 51.939, 51.936, 52.911, 51.945, 51.916, 51.905, 52.956, 49.971] + [43.300, 40.290, 41.305, 43.277, 43.506, 43.276, 43.430, 41.060, 43.300, 43.263] + [35.722, 31.013, 34.743, 33.502, 34.294, 33.903, 33.720, 33.677, 34.385, 33.140]  + [27.523, 25.958, 26.819, 25.479, 26.125, 25.501, 26.177, 25.894,26.190, 25.120] + [19.024, 17.551, 19.023, 18.995, 19.046, 19.961, 19.642, 18.589, 19.985, 19.732]   # HostCC吞吐量 (mpps)
thpt_exp = [79.272, 79.103, 79.473, 78.025, 77.429, 78.309, 79.702, 79.767, 79.835, 79.041] + [77.465, 76.834, 76.495, 76.747, 75.358, 76.503, 76.168, 76.352, 75.453, 75.081] + [72.363, 71.744, 70.303, 70.421, 70.468, 70.734, 68.204, 69.493, 69.345, 69.234] + [67.072, 63.853, 62.753, 63.395, 63.846, 63.363, 62.842, 63.759, 64.238, 63.682] + [58.649, 56.204, 56.528, 55.347, 55.498, 55.103, 54.145, 54.222, 55.963, 55.321]  # 最优性能 (mpps)

# 绘制图形
plt.figure(figsize=(10, 4))
plt.plot(time, thpt_base, label="Baseline", color="black", linestyle="-", marker="o", markersize=4)
plt.plot(time, thpt_shring, label="Optimized by ShRing", color="green", linestyle="-", marker="v", markersize=4)
plt.plot(time, thpt_hostcc, label="Optimized by HostCC", color="blue", linestyle="-", marker="d", markersize=4)
plt.plot(time, thpt_exp, label="Optimized by CEIO", color="orange", linestyle="-", marker="*", markersize=4)

# 添加垂直线和注释
events = [0, 10, 20, 30, 40, 50]  # 事件发生的时间点
labels = ["8 original flows", "2 burst flows", "4 burst flows",
          "6 burst flows", "8 burst flows"]


# 添加阶段标签
for i in range(len(labels)):  # 确保索引不会越界
    x_mid = (events[i] + events[i+1]) / 2  # 当前阶段的中点
    plt.text(x_mid, 10, labels[i], ha="center", va="center", fontsize=11, bbox=dict(facecolor='white', alpha=0.5))


for x in events[1:-1]:  # 不在边界位置添加垂直线
    plt.axvline(x=x, color="gray", linestyle="--", linewidth=1)

# 设置轴标签和标题
plt.xlabel("Time (s)", fontsize=14)
plt.ylabel("Throughput (Mpps)", fontsize=14)
# plt.title("Performance under different level network burst", fontsize=14)

# 图例
plt.legend(loc="upper right",  bbox_to_anchor=(1.05, 1.15),  # 调整图例位置
              ncol=4,                      # 图例列数
              fontsize=12,                 # 字体大小
              frameon=False)

# 设置网格线
plt.grid(True, linestyle="--", alpha=0.6)


# 手动设置 y 轴范围，确保显示 0 到 10
plt.ylim(0, 85)  # 根据需要调整y轴的显示范围

# 显示图形
# plt.tight_layout()
# plt.show()
# print(plt.rcParams['font.family'])


if output == 'show':
    plt.show()
else:
    # output_path = '/Users/bowen/Documents/HKUST/acclio/paper/ACCLIO/figs/evaluation/'  # 修改为你的实际路径
    plt.savefig( branch + '.pdf', bbox_inches='tight')