import matplotlib.pyplot as plt
import numpy as np
from matplotlib import gridspec

branch = 'Queue' # ['Core', 'Queue', 'Batch']
output = 'show' # ['show', 'save'] 

# -----------------------source data in PipeTune-----------------------
# -------Core Num-------
Core_TACC = np.array([26.766, 25.079, 27.626, 24.313])
Core_Desktop = np.array([29.526, 35.317, 27.818, 27.92])
# -------Queue Num-------
Queue_TACC = np.array([24.313,11.238,17.175,19.103])
Queue_Desktop = np.array([30.247,25.61,29.789,34.597])
# -------Batch Num-------
Batch_TACC = np.array([26.089,25.079,24.596,25.519])
Batch_Desktop = np.array([33.89,35.317,31.493,26.369])


# -----------------------Fig configuration-----------------------
plt.rcParams['font.sans-serif'] = 'Times'
fig_width = 6
fig_height = 2.5
fig, ax = plt.subplots(figsize=(9.6, 4))    # ax: throughput

x_label_size = 28
y_label_size = 28
legend_size = 24
title_size = 28
orange = '#FE6331'  # orange
orange_dark = '#BF4B25'  # orange_dark
gray = '#E9E2EA'  # gray
gray_dark = '#848085'  # gray_dark
black = '#282D32'  # black
black_dark = '#000000'  # black_dark
white = '#FFFFFF'  # white
colomn_width = 0.2
colomn_gap = 0.05

# -----------------------Branch 1: core number-----------------------
if branch == 'Core':
    scale = 1
    x_labels = ['4', '8', '12', '16']
    label_ticks = range(len(x_labels))

    colomn_num_per_label = 2
    first_colomn_tick = np.array(range(len(x_labels))) - (colomn_width + colomn_gap) * (colomn_num_per_label - 1) / 2

    # draw colomns
    rects1 = ax.bar(first_colomn_tick, Core_Desktop * scale, color=orange, width=colomn_width, edgecolor=orange_dark, label='200G-server')
    rects2 = ax.bar(first_colomn_tick + colomn_width + colomn_gap, Core_TACC * scale, color=black, width=colomn_width, edgecolor=black_dark, label='100G-server')

    # draw lines
    line_desktop = ax.plot(first_colomn_tick, Core_Desktop * scale, marker='o', markersize=3, color=black, label='Variation curve')
    # line_tacc = ax.plot(first_colomn_tick + colomn_width + colomn_gap, Core_TACC * scale, marker='o', markersize=3, linestyle='--', color=black, label='Variation curve in 100G-server')

    # draw legend
    # plt.legend(loc='upper center', fontsize=legend_size, ncol=3)
    #plt.legend(fontsize=legend_size, ncol=3, frameon = False, bbox_to_anchor=(0.0, 1.01), loc=3, borderaxespad=0)

    plt.legend(fontsize=legend_size, ncol=1, frameon=False, loc='upper right', borderaxespad=0.5)


    # setup ticks
    upax_bottom = 20
    upax_top = 40

    ax.set_ylim(upax_bottom, upax_top)
    plt.yticks(fontsize=y_label_size)

    plt.yticks(range(20, 41, 5))
    ax.set_xticks(label_ticks)
    ax.set_xticklabels(x_labels, fontsize=x_label_size)

    ax.set_ylabel('Throughput (Mpps)', fontsize=title_size, fontweight='bold')
    # ax.set_xlabel('Changing core number', fontsize=title_size, fontweight='bold')

elif branch == 'Queue':
    scale = 1
    x_labels = ['4', '8', '12', '16']
    label_ticks = range(len(x_labels))

    colomn_num_per_label = 2
    first_colomn_tick = np.array(range(len(x_labels))) - (colomn_width + colomn_gap) * (colomn_num_per_label - 1) / 2

    # draw colomns
    rects1 = ax.bar(first_colomn_tick, Queue_Desktop * scale, color=orange, width=colomn_width, edgecolor=orange_dark, label='200G-server')
    rects2 = ax.bar(first_colomn_tick + colomn_width + colomn_gap, Queue_TACC * scale, color=black, width=colomn_width, edgecolor=black_dark, label='100G-server')

    # draw lines
    line_desktop = ax.plot(first_colomn_tick, Queue_Desktop * scale, marker='o', markersize=3, color=black, label='Variation curve')
    # line_tacc = ax.plot(first_colomn_tick + colomn_width + colomn_gap, Queue_TACC * scale, marker='o', markersize=3, linestyle='--', color=black, label='Variation curve in 100G-server')

    # draw legend
    # plt.legend(loc='upper right', fontsize=legend_size)
    #plt.legend(fontsize=legend_size, ncol=3, frameon = True, bbox_to_anchor=(0.05, 1.01), loc=3, borderaxespad=0)

    #plt.legend(fontsize=legend_size, ncol=2, frameon=False, loc='upper left', bbox_to_anchor=(0, 1), borderaxespad=0.5)

    # setup ticks
    upax_bottom = 8
    upax_top = 40
    ax.set_ylim(upax_bottom, upax_top)
    plt.yticks(fontsize=y_label_size)
    plt.yticks(range(10, 41, 10))
    ax.set_xticks(label_ticks)
    ax.set_xticklabels(x_labels, fontsize=x_label_size)

    ax.set_ylabel('Throughput (Mpps)', fontsize=title_size, fontweight='bold')
    # ax.set_xlabel('Changing queue number', fontsize=title_size, fontweight='bold')

elif branch == 'Batch':
    scale = 1
    x_labels = ['16', '32', '64', '128']
    label_ticks = range(len(x_labels))

    colomn_num_per_label = 2
    first_colomn_tick = np.array(range(len(x_labels))) - (colomn_width + colomn_gap) * (colomn_num_per_label - 1) / 2

    # draw colomns
    rects1 = ax.bar(first_colomn_tick, Batch_Desktop * scale, color=orange, width=colomn_width, edgecolor=orange_dark, label='200G-server')
    rects2 = ax.bar(first_colomn_tick + colomn_width + colomn_gap, Batch_TACC * scale, color=black, width=colomn_width, edgecolor=black_dark, label='100G-server')

    # draw lines
    line_desktop = ax.plot(first_colomn_tick, Batch_Desktop * scale, marker='o', markersize=3, color=black, label='Variation curve')
    # line_tacc = ax.plot(first_colomn_tick + colomn_width + colomn_gap, Batch_TACC * scale, marker='o', markersize=3, linestyle='--', color=black, label='Variation curve in 100G-server')

    # draw legend
    # plt.legend(loc='upper right', fontsize=legend_size) 
    #plt.legend(fontsize=legend_size, ncol=3, frameon = True, bbox_to_anchor=(0.05, 1.01), loc=3, borderaxespad=0)
    #plt.legend(fontsize=legend_size, ncol=1, frameon=False, loc='upper right', borderaxespad=0.5)

    # setup ticks
    upax_bottom = 20
    upax_top = 40
    ax.set_ylim(upax_bottom, upax_top)
    plt.yticks(fontsize=y_label_size)
    plt.yticks(range(20, 41, 5))
    ax.set_xticks(label_ticks)
    ax.set_xticklabels(x_labels, fontsize=x_label_size)

    ax.set_ylabel('Throughput (Mpps)', fontsize=title_size, fontweight='bold')
    # ax.set_xlabel('Changing batch number', fontsize=title_size, fontweight='bold')

if output == 'show':
    plt.show()
else:
    plt.savefig(branch+'.pdf', bbox_inches='tight')
