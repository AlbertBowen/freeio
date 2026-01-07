import matplotlib.pyplot as plt
import numpy as np
from matplotlib import gridspec

branch = 'eRPC-Size' # ['OVS-200G', 'eRPC-Machine', 'eRPC-Size']
output = 'show' # ['show', 'save'] 

# -----------------------experiments-----------------------
# -------ovs: 100G-------
tacc_ovs_base      = np.array([20,18,16])
tacc_pipe_base     = np.array([22,20,18])
tacc_ovs_tunning   = np.array([30,26,22])
tacc_pipe_tunning  = np.array([35,30,26])
# -------ovs: 200G-------
desk_ovs_base      = np.array([37.32,35.374,18.179])
desk_pipe_base     = np.array([39.821,34.732,15.761])
desk_ovs_tunning   = np.array([40.998,40.038,21.545])
desk_pipe_tunning  = np.array([41.739,38.257,21.244])
# -------erpc: vary machine-------
machine_baseline = np.array([18.667,16.394,22.263,27.76])
machine_tunning = np.array([21.48,16.394,44.59,40.153])
# -------erpc: vary size-------
size_baseline = np.array([17.736,9.973,18.667,9.634])
size_tunning = np.array([31.729,31.273,21.48,10.537])

# -----------------------Fig configuration-----------------------
plt.rcParams['font.sans-serif'] = 'Times'
fig_width = 6
fig_height = 2.5
fig, ax = plt.subplots(figsize=(10, 4))    # ax: throughput

x_label_size = 22
y_label_size = 22
legend_size = 20
title_size = 24
orange = '#FE6331'  # orange
orange_dark = '#BF4B25'  # orange_dark
gray = '#E9E2EA'  # gray
gray_dark = '#848085'  # gray_dark
black = '#282D32'  # black
black_dark = '#000000'  # black_dark
white = '#FFFFFF'  # white
colomn_width = 0.2
colomn_gap = 0.05

if branch == 'OVS-200G':
    colomn_width = 0.1
    colomn_gap = 0.02
    legend_size = 16.5
    scale = 1
    x_labels = ['128B', '256B', '1024B']
    label_ticks = range(len(x_labels))

    colomn_num_per_label = 4
    first_colomn_tick = np.array(range(len(x_labels))) - (colomn_width + colomn_gap) * (colomn_num_per_label - 1) / 2

    # draw colomns
    rects1 = ax.bar(first_colomn_tick, desk_ovs_base * scale, color=orange, width=colomn_width, edgecolor=orange_dark, label='Original OvS')
    rects2 = ax.bar(first_colomn_tick + colomn_width + colomn_gap, desk_pipe_base * scale, color=white, width=colomn_width, edgecolor=black_dark, label='Emulated original OvS')
    rects3 = ax.bar(first_colomn_tick + 2*colomn_width + 2*colomn_gap, desk_pipe_tunning * scale, color=black, width=colomn_width, edgecolor=black_dark, label='Optimized OvS')
    rects4 = ax.bar(first_colomn_tick + 3*colomn_width + 3*colomn_gap, desk_pipe_tunning * scale, color=gray, width=colomn_width, edgecolor=gray_dark, label='Emulated optimized OvS')

    # draw lines
    # line_desktop = ax.plot(first_colomn_tick, Core_Desktop * scale, marker='o', markersize=3, color=black, label='Variation curve')
    # line_tacc = ax.plot(first_colomn_tick + colomn_width + colomn_gap, Core_TACC * scale, marker='o', markersize=3, linestyle='--', color=black, label='Variation curve in 100G-server')

    # draw legend
    plt.legend(fontsize=legend_size, ncol=1, frameon=False, loc='upper right', borderaxespad=0)

    # setup y label
    y_lable = ["0", "10", "20", "30", "40", "50"]
    y_tick = np.array([0, 10, 20, 30, 40, 50]) * scale
    ax.set_yticks(y_tick)
    ax.set_yticklabels(y_lable, fontsize=y_label_size)

    # setup x label
    ax.set_xticks(label_ticks)
    ax.set_xticklabels(x_labels, fontsize=x_label_size)

    #setup x/y name
    ax.set_ylabel('Throughput (Mpps)', fontsize=title_size)
elif branch == 'eRPC-Machine':
    scale = 1
    x_labels = ['100G DPDK', '100G RDMA', '200G DPDK', '200G RDMA']
    label_ticks = range(len(x_labels))

    colomn_num_per_label = 2
    first_colomn_tick = np.array(range(len(x_labels))) - (colomn_width + colomn_gap) * (colomn_num_per_label - 1) / 2

    # draw colomns
    line_rate = np.array([25, 25, 50, 50])
    rects1_line_rate = ax.bar(first_colomn_tick, line_rate * scale, color=white, width=colomn_width, edgecolor=black_dark, linestyle='dashed',label='Link Capacity', linewidth=1)
    rects1 = ax.bar(first_colomn_tick, machine_baseline * scale, color=orange, width=colomn_width, edgecolor=orange_dark, label='Original eRPC')
    rects2_line_rate = ax.bar(first_colomn_tick + colomn_width + colomn_gap, line_rate * scale, color=white, width=colomn_width, edgecolor=black_dark, linestyle='dashed', linewidth=1)
    rects2 = ax.bar(first_colomn_tick + colomn_width + colomn_gap, machine_tunning * scale, color=black, width=colomn_width, edgecolor=black_dark, label='Optimized eRPC')

    # draw legend
    plt.legend(fontsize=legend_size, ncol=1, frameon=False, loc='upper left', borderaxespad=0)

    # setup y label
    y_lable = ["0", "10", "20", "30", "40", "50"]
    y_tick = np.array([0, 10, 20, 30, 40, 50]) * scale
    ax.set_yticks(y_tick)
    ax.set_yticklabels(y_lable, fontsize=y_label_size)

    # setup x label
    ax.set_xticks(label_ticks)
    ax.set_xticklabels(x_labels, fontsize=x_label_size)

    #setup x/y name
    ax.set_ylabel('Throughput (Mpps)', fontsize=title_size)
    # ax.set_xlabel('Hardware modification', fontsize=title_size, fontweight='bold')

elif branch == 'eRPC-Size':
    scale = 1
    x_labels = ['128B', '256B', '512B', '1024B']
    label_ticks = range(len(x_labels))

    colomn_num_per_label = 2
    first_colomn_tick = np.array(range(len(x_labels))) - (colomn_width + colomn_gap) * (colomn_num_per_label - 1) / 2

    # draw colomns
    line_rate = np.array([25, 25, 50, 50])
    # rects1_line_rate = ax.bar(first_colomn_tick, line_rate * scale, color=white, width=colomn_width, edgecolor=black_dark, linestyle='dashed', linewidth=1)
    rects1 = ax.bar(first_colomn_tick, size_baseline * scale, color=orange, width=colomn_width, edgecolor=orange_dark, label='eRPC')
    # rects2_line_rate = ax.bar(first_colomn_tick + colomn_width + colomn_gap, line_rate * scale, color=white, width=colomn_width, edgecolor=black_dark, linestyle='dashed', linewidth=1)
    rects2 = ax.bar(first_colomn_tick + colomn_width + colomn_gap, size_tunning * scale, color=black, width=colomn_width, edgecolor=black_dark, label='eRPC after tunning')

    # setup y axis
    y_lable = ["0", "10", "20", "30", "40"]
    y_tick = np.array([0, 10, 20, 30, 40]) * scale
    ax.set_yticks(y_tick)
    ax.set_yticklabels(y_lable, fontsize=y_label_size)

    # setup x axis
    ax.set_xticks(label_ticks)
    ax.set_xticklabels(x_labels, fontsize=x_label_size)

    ax.set_ylabel('Throughput (Mpps)', fontsize=title_size)
    # ax.set_xlabel('Hardware modification', fontsize=title_size, fontweight='bold')


if output == 'show':
    plt.show()
else:
    plt.savefig(branch+'.pdf', bbox_inches='tight')
