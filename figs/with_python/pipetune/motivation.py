import matplotlib.pyplot as plt
import numpy as np

branch = 'hardware_changes' # ['hardware_changes', 'workload_changes', 'core_allocation']
output = 'save' # ['show', 'save'] 

# -----------------------source data in eRPC echo mode-----------------------
# TACC
# core 1 ~ 16
TACC_64_dpdk = np.array([-1, -1, -1, -1, 29.565])
TACC_128_dpdk = np.array([-1, -1, -1, -1, 17.736])
TACC_256_dpdk = np.array([-1, -1, -1, -1, 9.973])
TACC_512_dpdk = np.array([-1, -1, -1, -1, 18.753])
TACC_1024_dpdk = np.array([-1, -1, -1, -1, 9.634])

TACC_64_rdma = np.array([])
TACC_128_rdma = np.array([])
TACC_256_rdma = np.array([])
TACC_512_rdma = np.array([-1, -1, -1, -1, 16.394])
TACC_1024_rdma = np.array([])

# P50 P99 P99.9
TACC_64_dpdk_lat_c16 = np.array([16.97, 29.13, 37.19])
TACC_128_dpdk_lat_c16 = np.array([28.73, 38.35, 46.05])
TACC_256_dpdk_lat_c16 = np.array([51.28, 61.93, 68.53])
TACC_512_dpdk_lat_c16 = np.array([27.03, 39.37, 52.22])
TACC_1024_dpdk_lat_c16 = np.array([49.69, 65.65, 73.39])

TACC_64_rdma_lat_c16 = np.array([])
TACC_128_rdma_lat_c16 = np.array([])
TACC_256_rdma_lat_c16 = np.array([])
TACC_512_rdma_lat_c16 = np.array([31.22, 46.86, 55.24])
TACC_1024_rdma_lat_c16 = np.array([])

# Desktop
Desk_64_dpdk = np.array([7.916, 15.404, 29.652, 40.685, 37.095])
Desk_128_dpdk = np.array([])
Desk_256_dpdk = np.array([])
Desk_512_dpdk = np.array([7.542, 14.059, 24.845, 35.932, 22.263])
Desk_1024_dpdk = np.array([])

Desk_64_rdma = np.array([11.672, 23.287, 44.748, 72.742, 82.521])
Desk_128_rdma = np.array([])
Desk_256_rdma = np.array([])
Desk_512_rdma = np.array([9.507, 17.717, 28.184, 20.629, 27.76])
Desk_1024_rdma = np.array([])

# P50 P99 P99.9
Desk_64_dpdk_lat_c16 = np.array([])
Desk_128_dpdk_lat_c16 = np.array([])
Desk_256_dpdk_lat_c16 = np.array([])
Desk_512_dpdk_lat_c1 = np.array([17.9, 20.3, 26.4])
Desk_512_dpdk_lat_c2 = np.array([18.65, 20.85, 24.95])
Desk_512_dpdk_lat_c4 = np.array([21.5, 25.65, 31.6])
Desk_512_dpdk_lat_c8 = np.array([29.962, 36.125, 45.487])
Desk_512_dpdk_lat_c16 = np.array([92.14, 109.28, 128.94])
Desk_1024_dpdk_lat_c16 = np.array([])

Desk_64_rdma_lat_c16 = np.array([])
Desk_128_rdma_lat_c16 = np.array([])
Desk_256_rdma_lat_c16 = np.array([])
Desk_512_rdma_lat_c1 = np.array([14.5, 15.4, 19.4])
Desk_512_rdma_lat_c2 = np.array([14.9, 16.2, 20.8])
Desk_512_rdma_lat_c4 = np.array([18.15, 21.25, 26.18])
Desk_512_rdma_lat_c8 = np.array([32.64, 42.55, 59])
Desk_512_rdma_lat_c16 = np.array([71.68, 130.75, 200.66])
Desk_1024_rdma_lat_c16 = np.array([])

# DThub
DThub_64_dpdk = np.array([])
DThub_128_dpdk = np.array([])
DThub_256_dpdk = np.array([])
DThub_512_dpdk = np.array([])
DThub_1024_dpdk = np.array([])

DThub_64_rdma = np.array([])
DThub_128_rdma = np.array([])
DThub_256_rdma = np.array([])
DThub_512_rdma = np.array([])
DThub_1024_rdma = np.array([])

DThub_64_lat_c1 = np.array([28, 50.6, 58.1])
DThub_128_lat_c1 = np.array([33.3, 36.8, 59])
DThub_256_lat_c1 = np.array([63, 64.9, 106.4])
DThub_512_lat_c1 = np.array([29.7, 34.8, 93.6])
DThub_1024_lat_c1 = np.array([31.3, 36.6, 48.6])

# -----------------------Fig configuration-----------------------
plt.rcParams['font.sans-serif'] = 'Times'
# plt.rcParams['text.usetex'] = True
# plt.rcParams['text.latex.preamble'] = r'\usepackage{times}'
fig, ax = plt.subplots(figsize=(8, 2.7))    # ax: throughput
ax2 = ax.twinx()                            # ax2: latency
x_label_size = 18
y_label_size = 18
legend_size = 16
title_size = 18
orange = '#FE6331'  # orange
orange_dark = '#BF4B25'  # orange_dark
gray = '#E9E2EA'  # gray
gray_dark = '#848085'  # gray_dark
black = '#282D32'  # black
black_dark = '#000000'  # black_dark
white = '#FFFFFF'  # white
colomn_width = 0.2
colomn_gap = 0.05

# -----------------------Branch 1: hardware_changes-----------------------
if branch == 'hardware_changes':
    scale = 0.6
    x_labels = ['100Gbps\nDPDK', '100Gbps\nRDMA', '200Gbps\nDPDK', '200Gbps\nRDMA']
    label_ticks = range(len(x_labels))

    colomn_num_per_label = 2
    first_colomn_tick = np.array(range(len(x_labels))) - (colomn_width + colomn_gap) * (colomn_num_per_label - 1) / 2

    # draw throughput colomns
    line_rate = np.array([25, 25, 50, 50])
    tp_group = np.array([TACC_512_dpdk[4], TACC_512_rdma[4], Desk_512_dpdk[4], Desk_512_rdma[4]])
    rects1_line_rate = ax.bar(first_colomn_tick, line_rate * scale, color=white, width=colomn_width, edgecolor=black_dark, linestyle='dashed', linewidth=1)
    rects1 = ax.bar(first_colomn_tick, tp_group * scale, color=orange, width=colomn_width, edgecolor=orange_dark)

    # draw latency boxes
    lat_group = [TACC_512_dpdk_lat_c16, TACC_512_rdma_lat_c16, Desk_512_dpdk_lat_c16, Desk_512_rdma_lat_c16]
    boxes = ax2.boxplot(lat_group, positions=first_colomn_tick+colomn_width+colomn_gap, widths=colomn_width, patch_artist=True, boxprops=dict(facecolor=gray, color=black), whiskerprops=dict(color=black), capprops=dict(color=black), medianprops=dict(color=black_dark))
    fake_lat_colomn = np.array([0, 0, 0, 0])
    fake_lat_rects = ax2.bar(first_colomn_tick+colomn_width+colomn_gap, fake_lat_colomn, color=gray, width=colomn_width, edgecolor=black)

    ax2.set_xticks([])
    plt.yticks(fontsize=y_label_size)
    ax.set_xticks(label_ticks)
    ax.set_xticklabels(x_labels, fontsize=x_label_size)

    # draw lines
    line_tp = ax.plot(first_colomn_tick, tp_group * scale, marker='o', markersize=3, color=black, label='Throughput')
    medians = [item.get_ydata()[0] for item in boxes['medians']]
    x_pos = first_colomn_tick+colomn_width+colomn_gap
    # line_lat = ax2.plot(x_pos, medians, marker='o', markersize=1, linestyle='--', color=gray_dark, label='Latency')

    # draw legend
    #plt.legend([rects1_line_rate, rects1, fake_lat_rects], ['Link Capacity', 'Throughput', 'Latency'], fontsize=legend_size, ncol=3, frameon = False, bbox_to_anchor=(0.5, 1.01), loc=3, borderaxespad=0)

    #plt.legend([rects1_line_rate,rects1, fake_lat_rects], ['Link Capacity', 'Throughput', 'Latency'], fontsize=legend_size, ncol=3, frameon = False, bbox_to_anchor=(0, 0.8), loc=3, borderaxespad=0)

    plt.legend([rects1_line_rate, rects1, fake_lat_rects], ['Link Capacity', 'Throughput', 'Latency'], fontsize=legend_size, ncol=1, frameon=False, bbox_to_anchor=(0, 1), loc='upper left', borderaxespad=0)

    # ax.legend(fontsize=10, ncol=2, frameon = True, bbox_to_anchor=(0.0, 1.01), loc=3, borderaxespad=0)
    # ax2.legend(fontsize=10, ncol=2, frameon = True, bbox_to_anchor=(0.5, 1.01), loc=3, borderaxespad=0)

    ax.set_ylabel('Throughput (Mrps)', fontsize=title_size, fontweight='bold')
    #ax.set_xlabel('Hardware Motification', fontsize=title_size, fontweight='bold')
    ax2.set_ylabel('Latency (μs)', fontsize=title_size, fontweight='bold')

    y_lable = ["0", "10", "20", "30", "40", "50"]
    y_tick = np.array([0, 10, 20, 30, 40, 50]) * scale
    ax.set_yticks(y_tick)
    ax.set_yticklabels(y_lable, fontsize=y_label_size)

# -----------------------Branch 2: workload_changes-----------------------
elif branch == 'workload_changes':
    scale = 0.6
    x_labels = ['64B', '128B', '256B', '512B', '1024B']
    label_ticks = range(len(x_labels))

    colomn_num_per_label = 2
    first_colomn_tick = np.array(range(len(x_labels))) - (colomn_width + colomn_gap) * (colomn_num_per_label - 1) / 2

    # draw throughput colomns
    tp_group = np.array([TACC_64_dpdk[4], TACC_128_dpdk[4], TACC_256_dpdk[4], TACC_512_dpdk[4], TACC_1024_dpdk[4]])
    rects1 = ax.bar(first_colomn_tick, tp_group * scale, color=orange, width=colomn_width, edgecolor=orange_dark)

    # draw latency boxes
    lat_group = [TACC_64_dpdk_lat_c16, TACC_128_dpdk_lat_c16, TACC_256_dpdk_lat_c16, TACC_512_dpdk_lat_c16, TACC_1024_dpdk_lat_c16]
    boxes = ax2.boxplot(lat_group, positions=first_colomn_tick+colomn_width+colomn_gap, widths=colomn_width, patch_artist=True, boxprops=dict(facecolor=gray, color=black), whiskerprops=dict(color=black), capprops=dict(color=black), medianprops=dict(color=black_dark))
    fake_lat_colomn = np.array([0, 0, 0, 0, 0])
    fake_lat_rects = ax2.bar(first_colomn_tick+colomn_width+colomn_gap, fake_lat_colomn, color=gray, width=colomn_width, edgecolor=black)

    ax2.set_xticks([])
    plt.yticks(fontsize=y_label_size)
    ax.set_xticks(label_ticks)
    ax.set_xticklabels(x_labels, fontsize=x_label_size)

    # draw lines
    line_tp = ax.plot(first_colomn_tick, tp_group * scale, marker='o', markersize=3, color=black, label='Throughput')

    plt.legend([rects1, fake_lat_rects], ['Throughput', 'Latency'], fontsize=legend_size, ncol=2, frameon = False, bbox_to_anchor=(0, 0.8), loc=3, borderaxespad=0)

    y_lable = ["0", "10", "20", "30", "40"]
    y_tick = np.array([0, 10, 20, 30, 40]) * scale
    ax.set_yticks(y_tick)
    ax.set_yticklabels(y_lable, fontsize=y_label_size)
    y2_lable = ["0", "20", "40", "60", "80"]
    y2_tick = np.array([0, 20, 40, 60, 80])
    ax2.set_yticks(y2_tick)
    ax2.set_yticklabels(y2_lable, fontsize=y_label_size)

    ax.set_ylabel('Throughput (Mrps)', fontsize=title_size, fontweight='bold')
    #ax.set_xlabel('Workload Adjustment', fontsize=title_size, fontweight='bold')
    ax2.set_ylabel('Latency (μs)', fontsize=title_size, fontweight='bold')
    fig.subplots_adjust(left=0.14, right=0.87, top=0.9, bottom=0.1)

# -----------------------Branch 3: core allocation-----------------------
elif branch == 'core_allocation':
    scale = 0.6
    x_labels = ['1', '2', '4', '8', '16']
    label_ticks = range(len(x_labels))

    colomn_num_per_label = 4    # dpdk_tp + dpdk_lat + rdma_tp + rdma_lat
    first_colomn_tick = np.array(range(len(x_labels))) - (colomn_width + colomn_gap) * (colomn_num_per_label - 1) / 2

    # draw throughput colomns
    rects1 = ax.bar(first_colomn_tick, Desk_512_dpdk * scale, color=orange, width=colomn_width, edgecolor=orange_dark)
    rects2 = ax.bar(first_colomn_tick + (colomn_width + colomn_gap) * 2, Desk_512_rdma * scale, color=black, width=colomn_width, edgecolor=black_dark)

    # draw legend
    plt.legend([rects1, rects2], ['200G-server w/o RDMA', '200G-server with RDMA'], fontsize=10, ncol=2, frameon = True, bbox_to_anchor=(0.07, 1.01), loc=3, borderaxespad=0)

    # draw latency boxes
    lat_group = [Desk_512_dpdk_lat_c1, Desk_512_dpdk_lat_c2, Desk_512_dpdk_lat_c4, Desk_512_dpdk_lat_c8, Desk_512_dpdk_lat_c16]
    boxes = ax2.boxplot(lat_group, positions=first_colomn_tick+colomn_width+colomn_gap, widths=colomn_width, patch_artist=True, boxprops=dict(facecolor=gray, color=black), whiskerprops=dict(color=black), capprops=dict(color=black), medianprops=dict(color=black_dark))
    lat_group = [Desk_512_rdma_lat_c1, Desk_512_rdma_lat_c2, Desk_512_rdma_lat_c4, Desk_512_rdma_lat_c8, Desk_512_rdma_lat_c16]
    boxes = ax2.boxplot(lat_group, positions=first_colomn_tick+(colomn_width + colomn_gap) * 3, widths=colomn_width, patch_artist=True, boxprops=dict(facecolor=gray, color=black), whiskerprops=dict(color=black), capprops=dict(color=black), medianprops=dict(color=black_dark))

    ax2.set_xticks([])
    ax.set_xticks(label_ticks)
    ax.set_xticklabels(x_labels)

    y_lable = ["0", "10", "20", "30", "40"]
    y_tick = np.array([0, 10, 20, 30, 40]) * scale
    ax.set_yticks(y_tick)
    ax.set_yticklabels(y_lable)

    ax.set_ylabel('Throughput (Mrps)', fontsize=12, fontweight='bold')
    ax.set_xlabel('Core Allocation', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Latency (μs)', fontsize=12, fontweight='bold')
    fig.subplots_adjust(left=0.14, right=0.87, top=0.9, bottom=0.1)
# -----------------------Output-----------------------
if output == 'show':
    plt.show()
else:
    print(branch+'.pdf')
    plt.savefig(branch+'.pdf', bbox_inches='tight')