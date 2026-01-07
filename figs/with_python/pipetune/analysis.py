import matplotlib.pyplot as plt
import numpy as np
from matplotlib import gridspec

branch = 'Batch' # ['Core', 'Queue', 'Batch']
sub_branch = 'LApp' # ['LApp', 'MApp', 'TApp]
output = 'save' # ['show', 'save'] 

# -----------------------source data in PipeTune-----------------------
# -------Core Num-------
# core 1 ~ 16, avg, min, max stall
Core_LApp_C1_stall = np.array([[0.094, 0.034, 3.795],
                           [0.22, 0.035, 10.082],
                           [0.39, 0.034, 24.389],
                           [0.89, 0.036, 141.326],
                           [3.62, 0.049, 201.797]])
Core_MApp_C2_comp_time = np.array([[9.747, 9.188, 42.957],
                                  [9.789, 9.115, 45.371],
                                  [10.274, 9.147, 159.325],
                                  [11.001, 9.893, 346.854],
                                  [15.407, 12.097, 746.778]])
Core_MApp_C2_St_cache_miss = np.array([0.0, 0.05, 0.38, 0.64, 0.73])
# -------Queue Num-------
# queue 1 ~ 16, avg, min, max stall
Queue_LApp_C3C4_comp_time = np.array([[4.186, 4.774, 10.441],
                                  [5.523, 4.176, 25.344],
                                  [7.905, 4.169, 47.585],
                                  [11.781, 4.824, 163.234],
                                  [21.256, 12.404, 263.448]])
Queue_LApp_C3C4_cache_miss = np.array([0, 0.03, 0.23, 0.59, 0.78])
Queue_LApp_C3C4_IO_miss = np.array([0, 0.0840, 0.5970, 0.8060, 0.9290])
Queue_TApp_C3C4_comp_time = np.array([[9.809, 7.211, 24.12],
                                  [16.202, 10.915, 83.86],
                                  [20.882, 13.087, 168.154],
                                  [23.306, 14.983, 184.989],
                                  [34.828, 19.093, 450.828]])
Queue_TApp_C3C4_cache_miss = np.array([0.03, 0.16, 0.37, 0.41, 0.44])
Queue_TApp_C3C4_IO_miss = np.array([0.5070, 0.9140,	0.9890,	0.9910,	0.9860])
# -------Batch Size-------
Batch_TApp_C4_comp_time = np.array([[4.268, 2.51, 35.896],
                                  [9.663, 5.766, 77.842],
                                  [20.882, 13.087, 168.154],
                                  [44.485, 29.415, 202.866],
                                  [100.208, 69.08, 303.301]])
Batch_TApp_C4_cache_miss = np.array([0.12, 0.23, 0.37, 0.47, 0.68])
Batch_TApp_C4_IO_miss = np.array([0.9930, 0.9870,	0.9890,	0.9890,	0.9910])
Batch_LApp_C1_stall = np.array([[0.89, 0.036, 141.326],
                           [1.01, 0.099, 131.889],
                           [1.31, 0.205, 26.61],
                           [2.28, 0.404, 17.001],
                           [4.17, 0.921, 17.062]])

# -----------------------Fig configuration-----------------------
plt.rcParams['font.sans-serif'] = 'Times'
fig_width = 6
fig_height = 3.1
fig = plt.figure(figsize=(9.6, 4))  
if branch == 'Core' and sub_branch == 'LApp':   
    gs = gridspec.GridSpec(2, 1, height_ratios=[3, 1], hspace=0.1)
else:
    gs = gridspec.GridSpec(2, 1, height_ratios=[1, 3], hspace=0.1)
ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1], sharex=ax1)
fig.subplots_adjust(hspace=0.03)

# prepare twinned axes
if (not (branch == 'Core' and sub_branch == 'LApp')) and (not (branch == 'Batch' and sub_branch == 'LApp')):
    ax3 = ax1.twinx()
    ax4 = ax2.twinx()
    ax3.spines['bottom'].set_visible(False)
    ax4.spines['top'].set_visible(False)
# turn off spines
ax1.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)

# ax1&2: pipe stage duration / pipeline stall; ax3&4: memory access degradation / mempool usage

# setup ticks
ax1.tick_params(bottom=False)
ax2.tick_params(bottom=True)

# plotting break diagonals
d = 0.01  # line length 
ax1.plot((-d, +d), (-d, +d), c='k', clip_on=False, transform=ax1.transAxes)
ax1.plot((1 - d, 1 + d), (-d, +d), c='k', clip_on=False, transform=ax1.transAxes)
ax2.plot((-d, +d), (1 - d, (1 + d)), c='k', clip_on=False, transform=ax2.transAxes)
ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), c='k', clip_on=False, transform=ax2.transAxes)

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

# -----------------------Branch 1: Core Num-----------------------
if branch == 'Core':
    if sub_branch == 'LApp':
        # set limits for left y-axis
        upax1_bottom = 15
        upax1_top = 210
        ax1.set_ylim(upax1_bottom, upax1_top)
        upax2_bottom = 0
        upax2_top = 11
        ax2.set_ylim(upax2_bottom, upax2_top)
        
        # calculate x-position for each column
        scale = 1
        x_labels = ['1', '2', '4', '8', '16']
        label_ticks = range(len(x_labels))

        colomn_num_per_label = 1
        first_colomn_tick = np.array(range(len(x_labels))) - (colomn_width + colomn_gap) * (colomn_num_per_label - 1) / 2

        # Draw colomns for pipe stall duration
        rects1_high = ax1.bar(first_colomn_tick, Core_LApp_C1_stall[:, 2] * scale, colomn_width, color=orange, edgecolor=black)
        rects1_low = ax2.bar(first_colomn_tick, Core_LApp_C1_stall[:, 2] * scale, colomn_width, color=orange, edgecolor=black)
        rects2 = ax2.bar(first_colomn_tick, Core_LApp_C1_stall[:, 0] * scale, colomn_width, color=black, edgecolor=black)
        rects3 = ax2.bar(first_colomn_tick, Core_LApp_C1_stall[:, 1] * scale, colomn_width, color=gray, edgecolor=black)

        # set ticks and labels
        ax2.set_xticks(label_ticks)
        ax2.set_xticklabels(x_labels, fontsize=x_label_size)
        ax1.tick_params(axis='y', labelsize=y_label_size)
        ax2.tick_params(axis='y', labelsize=y_label_size)
        fig.text(0.05, 0.5, 'Pipeline stall (μs)', ha='center', va='center', rotation='vertical', fontsize=title_size, fontweight='bold')
        fig.text(0.99, 0.5, ' ', ha='center', va='center', rotation='vertical', fontsize=title_size, fontweight='bold')
        ax2.set_xlabel('CPU core number', fontsize=title_size, fontweight='bold')
        fig.subplots_adjust(left=0.14, right=0.87, top=0.9, bottom=0.1)
        # set legend
        plt.legend([rects3, rects2, rects1_low], ['P1', 'P50', 'P99'], fontsize=legend_size, ncol=3, frameon = False, bbox_to_anchor=(0.09,4.06), loc=3, borderaxespad=0)

    elif sub_branch == 'MApp':
        # set limits for left y-axis
        upax1_bottom = 100
        upax1_top = 800

        ax1.set_ylim(300, upax1_top)
        upax2_bottom = 0
        upax2_top = 80
        ax2.set_ylim(upax2_bottom, 100)
        # set limits for right y-axis
        # upax3_bottom = 1
        # upax3_top = 1
        # ax3.set_ylim(upax3_bottom, upax3_top)
        upax4_bottom = 0
        upax4_top = 1
        ax4.set_ylim(upax4_bottom, upax4_top)

        # calculate x-position for each column
        scale = 1
        x_labels = ['1', '2', '4', '8', '16']
        label_ticks = range(len(x_labels))

        colomn_num_per_label = 1
        first_colomn_tick = np.array(range(len(x_labels))) - (colomn_width + colomn_gap) * (colomn_num_per_label - 1) / 2

        # Draw colomns for pipe stage duration
        rects1_high = ax1.bar(first_colomn_tick, Core_MApp_C2_comp_time[:, 2] * scale, colomn_width, color=orange, edgecolor=black)
        rects1_low = ax2.bar(first_colomn_tick, Core_MApp_C2_comp_time[:, 2] * scale, colomn_width, color=orange, edgecolor=black)
        rects2 = ax2.bar(first_colomn_tick, Core_MApp_C2_comp_time[:, 0] * scale, colomn_width, color=black, edgecolor=black)
        rects3 = ax2.bar(first_colomn_tick, Core_MApp_C2_comp_time[:, 1] * scale, colomn_width, color=gray, edgecolor=black)

        # Draw line for L3 cache miss
        ax4.plot(first_colomn_tick, Core_MApp_C2_St_cache_miss, marker='o', markersize=3, linestyle='--', color=black, label='L3 store miss rate')

        # set ticks and labels
        ax3.set_xticks([])
        ax3.set_yticks([])
        ax4.set_xticks([])
        ax4.set_yticks([0, 0.25, 0.5, 0.75, 1])
        ax4.set_yticklabels(['0%', "25%", "50%", "75%", "100%"], fontsize=y_label_size)
        ax2.set_xticks(label_ticks)
        ax2.set_xticklabels(x_labels, fontsize=x_label_size)
        ax1.tick_params(axis='y', labelsize=y_label_size)
        ax2.tick_params(axis='y', labelsize=y_label_size)
        fig.text(0.045, 0.5, 'Cmpl. time (μs)', ha='center', va='center', rotation='vertical', fontsize=title_size, fontweight='bold')
        fig.text(0.99, 0.5, 'Cache miss rate', ha='center', va='center', rotation='vertical', fontsize=title_size, fontweight='bold')
        ax2.set_xlabel('CPU core number', fontsize=title_size, fontweight='bold')
        fig.subplots_adjust(left=0.14, right=0.87, top=0.9, bottom=0.1)
        # set legend
        ax4.legend(fontsize=legend_size, bbox_to_anchor=(0.54, 1.50), frameon = False)
        ax2.legend([rects3, rects2, rects1_low], ['P1', 'P50', 'P99'], fontsize=legend_size, ncol=3, frameon = False, bbox_to_anchor=(0.09, 1.36), loc=3, borderaxespad=0)

# -----------------------Branch 2: Queue Num-----------------------
elif branch == 'Queue':
    if sub_branch == 'LApp':
        # set limits for left y-axis
        upax1_bottom = 200
        upax1_top = 300
        ax1.set_ylim(upax1_bottom, upax1_top)
        upax2_bottom = 0
        upax2_top = 50
        ax2.set_ylim(upax2_bottom, upax2_top)
        # set limits for right y-axis
        # upax3_bottom = 1
        # upax3_top = 1
        # ax3.set_ylim(upax3_bottom, upax3_top)
        upax4_bottom = 0
        upax4_top = 1
        ax4.set_ylim(upax4_bottom, upax4_top)

        # calculate x-position for each column
        scale = 1
        x_labels = ['1', '2', '4', '8', '16']
        label_ticks = range(len(x_labels))

        colomn_num_per_label = 1
        first_colomn_tick = np.array(range(len(x_labels))) - (colomn_width + colomn_gap) * (colomn_num_per_label - 1) / 2

        # Draw colomns for pipe stage duration
        rects1_high = ax1.bar(first_colomn_tick, Queue_LApp_C3C4_comp_time[:, 2] * scale, colomn_width, color=orange, edgecolor=black)
        rects1_low = ax2.bar(first_colomn_tick, Queue_LApp_C3C4_comp_time[:, 2] * scale, colomn_width, color=orange, edgecolor=black)
        rects2 = ax2.bar(first_colomn_tick, Queue_LApp_C3C4_comp_time[:, 0] * scale, colomn_width, color=black, edgecolor=black)
        rects3 = ax2.bar(first_colomn_tick, Queue_LApp_C3C4_comp_time[:, 1] * scale, colomn_width, color=gray, edgecolor=black)

        # Draw line for L3 cache miss and IO miss
        ax4.plot(first_colomn_tick, Queue_LApp_C3C4_cache_miss, marker='o', markersize=3, linestyle='--', color=black, label='L3 store miss rate')
        ax4.plot(first_colomn_tick, Queue_LApp_C3C4_IO_miss, marker='o', markersize=3, linestyle=':', color=black, label=' ItoM miss rate')

        # set ticks and labels
        ax3.set_xticks([])
        ax3.set_yticks([])
        ax4.set_xticks([])
        ax4.set_yticks([0, 0.25, 0.5, 0.75, 1])
        ax4.set_yticklabels(['0%', "25%", "50%", "75%", "100%"], fontsize=y_label_size)
        ax2.set_xticks(label_ticks)
        ax2.set_xticklabels(x_labels, fontsize=x_label_size)
        ax1.tick_params(axis='y', labelsize=y_label_size)
        ax2.tick_params(axis='y', labelsize=y_label_size)
        fig.text(0.05, 0.5, 'Cmpl. time (μs)', ha='center', va='center', rotation='vertical', fontsize=title_size, fontweight='bold')
        fig.text(0.99, 0.5, 'Cache/IO miss rate', ha='center', va='center', rotation='vertical', fontsize=title_size, fontweight='bold')
        ax2.set_xlabel('Enabled queue number', fontsize=title_size, fontweight='bold')
        fig.subplots_adjust(left=0.14, right=0.87, top=0.9, bottom=0.1)
        # set legend
        ax4.legend(fontsize=legend_size, bbox_to_anchor=(0.54, 1.50), frameon = False)
        ax2.legend([rects3, rects2, rects1_low], ['P1', 'P50', 'P99'], fontsize=legend_size, ncol=3, frameon = False, bbox_to_anchor=(0.09, 1.36), loc=3, borderaxespad=0)


        

    elif sub_branch == 'TApp':
        # set limits for left y-axis
        upax1_bottom = 150
        upax1_top = 500
        ax1.set_ylim(upax1_bottom, upax1_top)
        upax2_bottom = 0
        upax2_top = 100
        ax2.set_ylim(upax2_bottom, upax2_top)
        # set limits for right y-axis
        # upax3_bottom = 1
        # upax3_top = 1
        # ax3.set_ylim(upax3_bottom, upax3_top)
        upax4_bottom = 0
        upax4_top = 1
        ax4.set_ylim(upax4_bottom, upax4_top)

        # calculate x-position for each column
        scale = 1
        x_labels = ['1', '2', '4', '8', '16']
        label_ticks = range(len(x_labels))

        colomn_num_per_label = 1
        first_colomn_tick = np.array(range(len(x_labels))) - (colomn_width + colomn_gap) * (colomn_num_per_label - 1) / 2

        # Draw colomns for pipe stage duration
        rects1_high = ax1.bar(first_colomn_tick, Queue_TApp_C3C4_comp_time[:, 2] * scale, colomn_width, color=orange, edgecolor=black)
        rects1_low = ax2.bar(first_colomn_tick, Queue_TApp_C3C4_comp_time[:, 2] * scale, colomn_width, color=orange, edgecolor=black)
        rects2 = ax2.bar(first_colomn_tick, Queue_TApp_C3C4_comp_time[:, 0] * scale, colomn_width, color=black, edgecolor=black)
        rects3 = ax2.bar(first_colomn_tick, Queue_TApp_C3C4_comp_time[:, 1] * scale, colomn_width, color=gray, edgecolor=black)

        # Draw line for L3 cache miss and IO miss
        ax4.plot(first_colomn_tick, Queue_TApp_C3C4_cache_miss, marker='o', markersize=3, linestyle='--', color=black, label='L3 load miss rate')
        ax4.plot(first_colomn_tick, Queue_TApp_C3C4_IO_miss, marker='o', markersize=3, linestyle=':', color=black, label=' ItoM miss rate')

        # set ticks and labels
        ax3.set_xticks([])
        ax3.set_yticks([])
        ax4.set_xticks([])
        ax4.set_yticks([0, 0.25, 0.5, 0.75, 1])
        ax4.set_yticklabels(['0%', "25%", "50%", "75%", "100%"], fontsize=y_label_size)
        ax2.set_xticks(label_ticks)
        ax2.set_xticklabels(x_labels, fontsize=x_label_size)
        ax1.tick_params(axis='y', labelsize=y_label_size)
        ax2.tick_params(axis='y', labelsize=y_label_size)
        fig.text(0.05, 0.5, 'Cmpl. time (μs)', ha='center', va='center', rotation='vertical', fontsize=title_size, fontweight='bold')
        fig.text(0.99, 0.5, 'Cache/IO miss rate', ha='center', va='center', rotation='vertical', fontsize=title_size, fontweight='bold')
        ax2.set_xlabel('Enabled queue number', fontsize=title_size, fontweight='bold')
        fig.subplots_adjust(left=0.143, right=0.87, top=0.9, bottom=0.1)


        # set legend
        ax4.legend(ncol=1,fontsize=legend_size, bbox_to_anchor=(0.53, 0.9), frameon = False)
        ax2.legend([rects3, rects2, rects1_low], ['P1', 'P50', 'P99'], fontsize=legend_size, ncol=3, frameon = False, bbox_to_anchor=(0.09, 1.36), loc=3, borderaxespad=0)



# -----------------------Branch 3: Batch size-----------------------
elif branch == 'Batch':
    if sub_branch == 'TApp':
        # set limits for left y-axis
        upax1_bottom = 110
        upax1_top = 350
        ax1.set_ylim(upax1_bottom, upax1_top)
        upax2_bottom = 0
        upax2_top = 110
        ax2.set_ylim(upax2_bottom, upax2_top)
        # set limits for right y-axis
        # upax3_bottom = 1
        # upax3_top = 1
        # ax3.set_ylim(upax3_bottom, upax3_top)
        upax4_bottom = 0
        upax4_top = 1
        ax4.set_ylim(upax4_bottom, upax4_top)

        # calculate x-position for each column
        scale = 0.9
        x_labels = ['32', '64', '128', '256', '512']
        label_ticks = range(len(x_labels))

        colomn_num_per_label = 1
        first_colomn_tick = np.array(range(len(x_labels))) - (colomn_width + colomn_gap) * (colomn_num_per_label - 1) / 2

        # Draw colomns for pipe stage duration
        rects1_high = ax1.bar(first_colomn_tick, Batch_TApp_C4_comp_time[:, 2] * scale, colomn_width, color=orange, edgecolor=black)
        rects1_low = ax2.bar(first_colomn_tick, Batch_TApp_C4_comp_time[:, 2] * scale, colomn_width, color=orange, edgecolor=black)
        rects2 = ax2.bar(first_colomn_tick, Batch_TApp_C4_comp_time[:, 0] * scale, colomn_width, color=black, edgecolor=black)
        rects3 = ax2.bar(first_colomn_tick, Batch_TApp_C4_comp_time[:, 1] * scale, colomn_width, color=gray, edgecolor=black)

        # Draw line for L3 cache miss and IO miss
        ax4.plot(first_colomn_tick, Batch_TApp_C4_cache_miss, marker='o', markersize=3, linestyle='--', color=black, label='L3 load miss rate')
        ax4.plot(first_colomn_tick, Batch_TApp_C4_IO_miss * scale, marker='o', markersize=3, linestyle=':', color=black, label=' ItoM miss rate')

        # set ticks and labels
        ax3.set_xticks([])
        ax3.set_yticks([])
        ax4.set_xticks([])
        ax4.set_yticks(np.array([0, 0.25, 0.5, 0.75, 1]) * scale)
        ax4.set_yticklabels(['0%', "25%", "50%", "75%", "100%"], fontsize=y_label_size)
        ax2.set_xticks(label_ticks)
        ax2.set_xticklabels(x_labels, fontsize=x_label_size)
        ax1.tick_params(axis='y', labelsize=y_label_size)
        ax2.tick_params(axis='y', labelsize=y_label_size)
        fig.text(0.05, 0.5, 'Cmpl. time (μs)', ha='center', va='center', rotation='vertical', fontsize=title_size, fontweight='bold')
        fig.text(0.99, 0.48, 'Cache/IO miss rate', ha='center', va='center', rotation='vertical', fontsize=title_size, fontweight='bold')
        ax2.set_xlabel('Batch processing size', fontsize=title_size, fontweight='bold')
        fig.subplots_adjust(left=0.14, right=0.87, top=0.9, bottom=0.1)
        # set legend
        ax4.legend(fontsize=legend_size,bbox_to_anchor=(0.54, 1.50), frameon = False,borderaxespad=0.5)
        ax2.legend([rects3, rects2, rects1_low], ['P1', 'P50', 'P99'], fontsize=legend_size, ncol=3, frameon = False, bbox_to_anchor=(0.09, 1.36), loc=3, borderaxespad=0)


    elif sub_branch == 'LApp':
        # set limits for left y-axis
        upax1_bottom = 100
        upax1_top = 150
        ax1.set_ylim(upax1_bottom, upax1_top)
        upax2_bottom = 0
        upax2_top = 30
        ax2.set_ylim(upax2_bottom, upax2_top)
        
        # calculate x-position for each column
        scale = 1
        x_labels = ['16', '32', '64', '128', '256']
        label_ticks = range(len(x_labels))

        colomn_num_per_label = 1
        first_colomn_tick = np.array(range(len(x_labels))) - (colomn_width + colomn_gap) * (colomn_num_per_label - 1) / 2

        # Draw colomns for pipe stall duration
        rects1_high = ax1.bar(first_colomn_tick, Batch_LApp_C1_stall[:, 2] * scale, colomn_width, color=orange, edgecolor=black)
        rects1_low = ax2.bar(first_colomn_tick, Batch_LApp_C1_stall[:, 2] * scale, colomn_width, color=orange, edgecolor=black)
        rects2 = ax2.bar(first_colomn_tick, Batch_LApp_C1_stall[:, 0] * scale, colomn_width, color=black, edgecolor=black)
        rects3 = ax2.bar(first_colomn_tick, Batch_LApp_C1_stall[:, 1] * scale, colomn_width, color=gray, edgecolor=black)

        # set ticks and labels
        ax2.set_xticks(label_ticks)
        ax2.set_xticklabels(x_labels, fontsize=x_label_size)
        ax1.tick_params(axis='y', labelsize=y_label_size)
        ax2.tick_params(axis='y', labelsize=y_label_size)
        fig.text(0.05, 0.5, 'Pipeline stall (μs)', ha='center', va='center', rotation='vertical', fontsize=title_size, fontweight='bold')
        fig.text(0.99, 0.5, ' ', ha='center', va='center', rotation='vertical', fontsize=title_size, fontweight='bold')
        ax2.set_xlabel('Batch processing size', fontsize=title_size, fontweight='bold')
        fig.subplots_adjust(left=0.14, right=0.87, top=0.9, bottom=0.1)
        # set legend
        ax2.legend([rects3, rects2, rects1_low], ['P1', 'P50', 'P99'], fontsize=legend_size, ncol=3, frameon = False, bbox_to_anchor=(0.09, 1.36), loc=3, borderaxespad=0)
# -----------------------Output-----------------------
if output == 'show':
    plt.show()
else:
    print('Saving figure...')
    plt.savefig(branch+'_'+sub_branch+'.pdf', bbox_inches='tight')
