import matplotlib.pyplot as plt
import numpy as np

output = 'save' # ['show', 'save'] 

# -----------------------Results-----------------------
small_interval = np.array([183.58, 183.48, 182.68, 180.58, 171.4, 164.4, 165.3, 164.9, 165.1])
middle_interval = np.array([182.58, 183.48, 182.68, 182.58, 179.58, 170.0, 165.9, 165.5, 165.1])
large_interval = np.array([184.556, 183.456, 182.856, 183.156, 184.556, 182.556, 183.556, 182.556, 183.556])

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


ax.plot(large_interval, label='Time slot: 1ms', color=black, linestyle='-', linewidth=2, marker='o', markersize=6)
# ax.plot(dperf, label='dperf', color=green, linestyle='-', linewidth=2)
ax.plot(middle_interval, label='Time slot: 500μs', color=orange_dark, linestyle='--', linewidth=2, marker='^', markersize=6, markerfacecolor=white)
ax.plot(small_interval, label='Time slot: 100μs', color=blue, linestyle='-.', linewidth=2, marker='s', markersize=6, markerfacecolor=white)

# plot line rate line


ax.set_xticks(label_ticks)
ax.set_xticklabels(x_labels, fontsize=x_label_size)
ax.set_yticks([150, 160, 170, 180, 190, 200])
ax.set_yticklabels([150, 160, 170, 180, 190, 200], fontsize=y_label_size)
ax.set_ylim(150, 200)

ax.grid(True, linestyle="--", alpha=0.6)

ax.legend(fontsize=legend_size, ncol=4, frameon=False, bbox_to_anchor=(0, 1), loc='upper left', borderaxespad=0)
ax.set_xlabel('Flow Number', fontsize=x_label_size)
ax.set_ylabel('Throughput (Gbps)', fontsize=y_label_size)
# ax.set_title('Throughput of Single Flow', fontsize=title_size)

if output == 'show':
    plt.show()
elif output == 'save':
    print('thousand_flow.pdf saved')
    plt.savefig('thousand_flow.pdf', bbox_inches='tight')



