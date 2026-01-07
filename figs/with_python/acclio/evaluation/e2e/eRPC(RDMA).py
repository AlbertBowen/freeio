import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

branch = 'eRPC(RDMA)' 
output = 'save' # ['show', 'save'] 


# -----------------------Fig configuration-----------------------
# plt.rcParams['font.sans-serif'] = 'Times'
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']  # 或者 'Nimbus Roman' / 'CMU Serif' 等 TrueType 字体
plt.rcParams['pdf.fonttype'] = 42  # 输出为 TrueType 字体，避免 Type3
plt.rcParams['ps.fonttype'] = 42
# plt.rcParams['text.usetex'] = True
# plt.rcParams['text.latex.preamble'] = r'\usepackage{times}'
fig, ax = plt.subplots(figsize=(8, 2.7))    # ax: throughput
ax2 = ax.twinx()                            # ax2: latency
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
if branch == 'eRPC(RDMA)':
    colomn_width = 0.15
colomn_gap = 0.05
group_gap = 0.1

# -----------------------Branch 3: core allocation-----------------------
if branch == 'eRPC(RDMA)':
    scale = 0.8
    x_labels = ['128B', '512B', '1024B']

    colomn_num_per_label = 4    # throughput of 4/8/12/16 cores
    label_ticks = np.array(range(len(x_labels))) + (colomn_width + colomn_gap) * (colomn_num_per_label - 1) / 2
    for i in range(len(label_ticks)):
        label_ticks[i] = label_ticks[i] + i * group_gap

    first_colomn_tick = label_ticks - (colomn_width + colomn_gap) * (colomn_num_per_label - 1) / 2

    # draw throughput colomns
    # max_tap_group = np.array([200, 200, 200, 200])
    ## draw eRPC throughput colomns
    eRPC_ticks = first_colomn_tick[0] + (colomn_width + colomn_gap) * np.array([0, 1, 2, 3])
    # rects1_line_rate = ax.bar(eRPC_ticks, max_tap_group * scale, color=white, width=colomn_width, edgecolor=black_dark, linestyle='dashed', linewidth=1, label='Line-rate Thrpt')
    
    tp_group = np.array([39.847, 52.036, 64.835, 79.982])

    
    # 设置不同方案的颜色
    colors = [grey, blue, green, yellow]
    for i, tick in enumerate(eRPC_ticks):
        ax.bar(tick, tp_group[i] * scale, color=colors[i], width=colomn_width, edgecolor=black, hatch='//')
    # per_core_tp = np.array([eRPC_Desk_512_dpdk[2]/4, eRPC_Desk_512_dpdk[3]/8, eRPC_Desk_512_dpdk[4]/12, eRPC_Desk_512_dpdk[5]/16])
    # line_per_core_tp = ax.plot(eRPC_ticks, per_core_tp * scale, marker='^', markersize=6, markerfacecolor=white, color=black, linestyle=':', label='Per-Flow Thrpt')
    ### draw eRPC cache miss rate
    cache_miss_group = np.array([69, 55, 8, 1])
    line_cache_miss = ax2.plot(eRPC_ticks, cache_miss_group, marker='^', markersize=6, markerfacecolor=white, color=black, label='Cache Miss Rate')


    ## draw OvS throughput colomns
    max_tap_group = np.array([50, 50, 50, 50])
    OvS_ticks = first_colomn_tick[1] + (colomn_width + colomn_gap) * np.array([0, 1, 2, 3])
    rects2_line_rate = ax.bar(OvS_ticks, max_tap_group * scale, color=white, width=colomn_width, edgecolor=black_dark, linestyle='dashed', linewidth=1, label='Line-rate Thrpt')
    tp_group = np.array([27.761, 28.947, 34.529, 40.153])
    
    # 设置不同方案的颜色
    for i, tick in enumerate(OvS_ticks):
        ax.bar(tick, tp_group[i] * scale, color=colors[i], width=colomn_width, edgecolor=black, hatch='//')
    # per_core_tp = np.array([OvS_Desk_512_dpdk[2]/4, OvS_Desk_512_dpdk[3]/8, OvS_Desk_512_dpdk[4]/12, OvS_Desk_512_dpdk[5]/16])
    # line_per_core_tp = ax.plot(OvS_ticks, per_core_tp * scale, marker='^', markersize=6, markerfacecolor=white, color=black, linestyle=':')
    ### draw OvS cache miss rate
    cache_miss_group = np.array([52, 30, 7, 2])
    line_cache_miss = ax2.plot(OvS_ticks, cache_miss_group, marker='^', markersize=6, markerfacecolor=white, color=black)
 

    ## draw LineFS throughput colomns\

    max_tap_group = np.array([25, 25, 25, 25])
    LineFS_ticks = first_colomn_tick[2] + (colomn_width + colomn_gap) * np.array([0, 1, 2, 3])
    rects3_line_rate = ax.bar(LineFS_ticks, max_tap_group * scale, color=white, width=colomn_width, edgecolor=black_dark, linestyle='dashed', linewidth=1)
    tp_group = np.array([16.343, 17.094, 18.831, 21.873])
    
    # 设置不同方案的颜色
    for i, tick in enumerate(LineFS_ticks):
        ax.bar(tick, tp_group[i] * scale, color=colors[i], width=colomn_width, edgecolor=black, hatch='//')
    # per_core_tp = np.array([LineFS_Desk_512_rdma[2]/4, LineFS_Desk_512_rdma[3]/8, LineFS_Desk_512_rdma[4]/12, LineFS_Desk_512_rdma[5]/16])
    # line_per_core_tp = ax.plot(LineFS_ticks, per_core_tp * scale, marker='^', markersize=6, markerfacecolor=white, color=black, linestyle=':')
    ### draw LineFS cache miss rate
    cache_miss_group = np.array([31, 24, 6, 2])
    line_cache_miss = ax2.plot(LineFS_ticks, cache_miss_group, marker='^', markersize=6, markerfacecolor=white, color=black)
    
 

    # 获取图例handles和labels
    handles1, labels1 = ax.get_legend_handles_labels()
    handles2, labels2 = ax2.get_legend_handles_labels()
    
    # 创建没有填充色的Throughput图例handle
    throughput_legend = Patch(facecolor='none', edgecolor='black', label='Throughput', hatch='//')
    
    # 重新排序handles和labels
    ordered_handles = [handles1[0], throughput_legend ] + handles2
    ordered_labels = [labels1[0], 'Throughput'] + labels2

    ax.grid(True, linestyle="--", alpha=0.6)
    
    # 更新图例
    ax.legend(ordered_handles, ordered_labels, fontsize=legend_size-1, ncol=4, frameon=False, bbox_to_anchor=(0.08, 1.01), loc=3, borderaxespad=0)

    
    # set ticks
    ax2.set_xticks([])
    ax2.set_yticks([0, 25, 50, 75, 100, 110])
    ax2.set_yticklabels(['0%', "25%", "50%", "75%", "100%", ""], fontsize=y_label_size)
  # 更新minor ticks
    labels_minor = ['Baseline', 'HostCC', 'ShRing', 'CEIO', 'Baseline', 'HostCC', 'ShRing', 'CEIO', 'Baseline', 'HostCC', 'ShRing', 'CEIO']
    labels_minor_ticks = np.concatenate([eRPC_ticks, OvS_ticks, LineFS_ticks])
    ax.set_xticks(labels_minor_ticks, minor=True)
    ax.set_xticklabels(labels_minor, minor=True,rotation=45)
    ax.set_xticks(label_ticks)
    ax.set_xticklabels(x_labels)
    ax.tick_params(axis='x', which='minor', length=0, labelsize=x_label_size - 2)
    ax.tick_params(axis='x', which='major', length=12, width=0, labelsize=x_label_size, pad=25)


    y_lable = ["0", "10", "20", "30", "40", "50", "60", "70", "80"]
    y_tick = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80]) * scale
    ax.set_yticks(y_tick)
    ax.set_yticklabels(y_lable, fontsize=y_label_size)

    ax.set_ylabel('Throughput (Mpps)', fontsize=title_size, fontweight='bold')
    ax2.set_ylabel('Cache Miss Rate', fontsize=title_size, fontweight='bold')









# -----------------------Output-----------------------
if output == 'show':
    plt.show()
else:
    print(branch+'.pdf')
    # output_path = '/Users/bowen/Documents/HKUST/acclio/paper/ACCLIO/figs/evaluation/'  # 修改为你的实际路径
    plt.savefig(branch + '.pdf', bbox_inches='tight')