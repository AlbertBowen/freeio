import matplotlib.pyplot as plt
import numpy as np

output = 'save' # ['show', 'save'] 

# -----------------------Results-----------------------
# perftest = np.array([2.90, 5.82, 11.77, 23.55, 47.10, 92.53, 155.08, 182.07, 183.58])
# dperf = np.array([9.70, 19.2, 37.9, 75.2, 150.58, 170.9, 182.3, 183.6, 184.0])
# fast_path = np.array([4.567, 8.563, 15.521, 31.457, 56.377, 95.304, 143.096, 182.214, 183.556])
perftest = np.array([4.567, 8.563, 15.521, 31.457, 56.377, 95.304, 143.096, 182.214, 183.556])
fast_path = np.array([2.90, 5.82, 11.77, 23.55, 47.10, 92.53, 155.08, 182.07, 183.58])
slow_path = np.array([2.378, 4.738, 9.617, 20.14, 41.965, 71.614, 147.465, 178.2, 180.3])

# -----------------------Fig configuration-----------------------
# plt.rcParams['font.sans-serif'] = 'Times'
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']  # 或者 'Nimbus Roman' / 'CMU Serif' 等 TrueType 字体
plt.rcParams['pdf.fonttype'] = 42  # 输出为 TrueType 字体，避免 Type3
plt.rcParams['ps.fonttype'] = 42
fig, ax = plt.subplots(figsize=(8, 2.7))
x_label_size = 14
y_label_size = 14
legend_size = 13
title_size = 18
orange = '#FE6331'  # orange
green = '#82B366'  # green
yellow = '#D6B656'  # yellow
blue = '#6C8EBF'  # blue
orange_dark = '#BF4B25'  # orange_dark
gray = '#E9E2EA'  # gray
gray_dark = '#848085'  # gray_dark
black = '#282D32'  # black
black_dark = '#000000'  # black_dark
grey = '#D9D9D9'  # grey
white = '#FFFFFF'  # white
pattern_1 = '\\\\'
pattern_2 = '//'
pattern_3 = '-.-.'
colomn_width = 0.17
colomn_gap = 0
group_gap = 0.03

# -----------------------Plot-----------------------
x_labels = ['64', '128', '256', '512', '1K', '2K', '4K', '8K', '16K']
label_ticks = np.arange(len(x_labels))

ax.plot(perftest, label='ib_write_bw', color=black, linestyle='-', linewidth=2, marker='o', markersize=6)
# ax.plot(dperf, label='dperf', color=green, linestyle='-', linewidth=2)
ax.plot(fast_path, label='fast path', color=orange_dark, linestyle='--', linewidth=2, marker='^', markersize=6, markerfacecolor=white)
ax.plot(slow_path, label='slow path', color=blue, linestyle='-.', linewidth=2, marker='s', markersize=6, markerfacecolor=white)

# plot line rate line


ax.set_xticks(label_ticks)
ax.set_xticklabels(x_labels, fontsize=x_label_size)
ax.set_yticks([0, 40, 80, 120, 160, 200])
ax.set_yticklabels([0, 40, 80, 120, 160, 200], fontsize=y_label_size)

ax.grid(True, linestyle="--", alpha=0.6)

ax.legend(fontsize=legend_size, ncol=4, frameon=False, bbox_to_anchor=(0, 1), loc='upper left', borderaxespad=0)
ax.set_xlabel('Message Size (B)', fontsize=x_label_size)
ax.set_ylabel('Throughput (Gbps)', fontsize=y_label_size)
# ax.set_title('Throughput of Single Flow', fontsize=title_size)

if output == 'show':
    plt.show()
elif output == 'save':
    print('single_flow.pdf saved')
    plt.savefig('single_flow.pdf', bbox_inches='tight')
