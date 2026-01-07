import matplotlib.pyplot as plt
import numpy as np
from matplotlib import gridspec


branch = 'eva_distribution' # ['burst', 'change_distribution']
output = 'save' # ['show', 'save'] 

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']  # 或 ['Nimbus Roman'] / ['CMU Serif']
plt.rcParams['pdf.fonttype'] = 42  # 用 TrueType 字体，防止 Type3
plt.rcParams['ps.fonttype'] = 42

# 数据
time = np.linspace(0, 50, 50)  # 时间轴，从0到60秒
thpt_base =[40.633, 40.846, 40.835, 40.833, 40.847, 40.884, 40.905, 40.901, 40.967, 40.965] + [35.695, 31.665, 31.678, 31.792, 30.946, 31.655, 31.613, 32.387, 31.648, 31.487] + [27.705, 20.255, 20.403, 20.438, 20.521, 20.731, 20.613, 21.184, 20.238, 20.697] + [15.597, 12.535, 12.377, 12.439, 12.432, 12.429, 12.445, 12.492, 12.476, 12.758]+ [9.749, 6.389, 6.355, 6.325, 6.407, 6.399, 6.952, 6.971, 6.526, 6.062]  # baseline (mpps)
thpt_shring = [69.599, 69.287, 68.913, 68.992, 68.891, 68.942, 68.840, 68.951, 68.823, 68.947] + [61.435, 57.958, 53.058, 51.164, 51.282, 51.133, 51.278, 51.425, 51.585, 51.667] + [44.107, 40.210, 33.072, 29.846, 30.797, 30.553, 30.379, 29.947, 29.956, 30.003] + [22.684, 21.479, 15.351, 14.238, 14.356, 13.242, 14.667, 14.813, 14.938, 15.117] + [13.248, 8.102, 8.069, 9.052, 8.192, 8.206, 7.829, 8.098, 8.209, 7.872]   # ShRing吞吐量 (mpps)
thpt_hostcc = [51.354, 52.264, 51.439, 51.936, 50.891, 52.311, 51.945, 51.224, 53.116, 50.905] + [41.237, 38.214, 40.514, 41.205, 41.208, 40.094, 40.629, 40.018, 40.693, 40.701] + [28.803, 25.258, 22.031, 24.013, 25.328, 26.296, 26.490, 26.599, 26.780, 26.009] + [19.308, 13.326, 12.488, 13.456, 13.461, 13.693, 13.691, 13.899, 13.890, 13.882] + [10.407, 7.198, 6.024, 6.802, 7.068, 6.602, 6.614, 6.600, 6.011, 6.386]   # HostCC吞吐量 (mpps)
thpt_exp = [79.654, 79.848, 79.630, 79.541, 79.746, 79.453, 78.260, 78.703, 79.645, 79.223] + [68.043, 61.047, 61.420, 60.635, 60.087, 61.570, 60.356, 60.485, 61.575, 61.309] + [47.479, 39.274, 37.575, 37.373, 36.436, 36.673, 37.354, 37.801, 36.664, 37.524] + [27.898, 22.963, 20.587, 20.744, 21.019, 21.305, 21.686, 20.747, 20.635, 20.128] + [15.405, 12.238, 11.640, 12.448, 11.046, 12.478, 12.584, 12.367, 12.457, 11.476]   # HostCC吞吐量 (mpps)
# 绘制图形
plt.figure(figsize=(10, 4))
plt.plot(time, thpt_base, label="Baseline", color="black", linestyle="-", marker="o", markersize=4)
plt.plot(time, thpt_shring, label="Optimized by ShRing", color="green", linestyle="-", marker="v", markersize=4)
plt.plot(time, thpt_hostcc, label="Optimized by HostCC", color="blue", linestyle="-", marker="d", markersize=4)
plt.plot(time, thpt_exp, label="Optimized by CEIO", color="orange", linestyle="-", marker="*", markersize=4)

# 添加垂直线和注释
events = [0, 10, 20, 30]  # 事件发生的时间点
labels = ["100%\nCPU-involved flows", "75%\nCPU-involved flows", "50%\nCPU-involved flows"]
# 添加阶段标签
for i in range(len(labels)):  # 确保索引不会越界
    x_mid = (events[i] + events[i+1]) / 2  # 当前阶段的中点
    plt.text(x_mid, 10, labels[i], ha="center", va="center", fontsize=9, bbox=dict(facecolor='white', alpha=0.5))


plt.text(45, 20, "12.5%\nCPU-involved flows", ha="center", va="center", fontsize=9, bbox=dict(facecolor='white', alpha=0.5))

plt.text(35, 10, "25%\nCPU-involved flow", ha="center", va="center", fontsize=9, bbox=dict(facecolor='white', alpha=0.5))


for x in events[1:-1]:  # 不在边界位置添加垂直线
    plt.axvline(x=x, color="gray", linestyle="--", linewidth=1)

# 设置轴标签和标题
plt.xlabel("Time (s)", fontsize=14)
plt.ylabel("Throughput (Mpps)", fontsize=14)
# plt.title("Performance under different flow distribution", fontsize=14)

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


if output == 'show':
    plt.show()
else:
    # output_path = '/Users/bowen/Documents/HKUST/CEIO/paper/ACCLIO/figs/evaluation/'  # 修改为你的实际路径
    plt.savefig(branch + '.pdf', bbox_inches='tight')