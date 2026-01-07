import matplotlib.pyplot as plt
import numpy as np

branch = 'LineFS' # ['varied_cores','LineFS']
output = 'show' # ['show', 'save'] 

# -----------------------source data in eRPC echo mode-----------------------
# TACC
# core 1 ~ 16
TACC_64_dpdk = np.array([-1, -1, -1, -1, 29.565])
TACC_128_dpdk = np.array([-1, -1, -1, -1, 17.736])
TACC_256_dpdk = np.array([-1, -1, -1, -1, 9.973])
eRPC_TACC_512_dpdk = np.array([-1, -1, -1, -1, 17.92])      # update
OvS_TACC_512_dpdk = np.array([-1, -1, -1, -1, 15.574])           # update #16
TACC_1024_dpdk = np.array([-1, -1, -1, -1, 9.634])

TACC_64_rdma = np.array([])
TACC_128_rdma = np.array([])
TACC_256_rdma = np.array([])
eRPC_TACC_512_rdma = np.array([-1, -1, -1, -1, 16.52])      # update
LineFS_TACC_512_rdma = np.array([-1, -1, -1, -1, 10.741])        # update #16
TACC_1024_rdma = np.array([])

# P50 P99 P99.9
TACC_64_dpdk_lat_c16 = np.array([16.97, 29.13, 37.19])
TACC_128_dpdk_lat_c16 = np.array([28.73, 38.35, 46.05])
TACC_256_dpdk_lat_c16 = np.array([51.28, 61.93, 68.53])
eRPC_TACC_512_dpdk_lat_c16 = np.array([28, 42.3, 55.8])     # update
OvS_TACC_512_dpdk_lat_c16 = np.array([0, 0, 0])             # todo
TACC_1024_dpdk_lat_c16 = np.array([49.69, 65.65, 73.39])

TACC_64_rdma_lat_c16 = np.array([])
TACC_128_rdma_lat_c16 = np.array([])
TACC_256_rdma_lat_c16 = np.array([])
eRPC_TACC_512_rdma_lat_c16 = np.array([30.8, 46.5, 54.3])       # update
LineFS_TACC_512_rdma_lat_c16 = np.array([0, 0, 0])              # todo
TACC_1024_rdma_lat_c16 = np.array([])

# Desktop
Desk_64_dpdk = np.array([7.916, 15.404, 29.652, 40.685, 37.095])
Desk_128_dpdk = np.array([])
Desk_256_dpdk = np.array([])
eRPC_Desk_512_dpdk = np.array([5.25, 7.9, 10.96, 17.6, 19.5, 20.96])       # update #1/2/4/8/12/16
eRPC_Desk_512_dpdk_cache_miss = np.array([0.05, 3.3, 53.8, 75.4, 86.8, 91])
OvS_Desk_512_dpdk = np.array([0, 0, 19.011, 30.250, 31.115, 27.623])                           # update
OvS_Desk_512_dpdk_cache_miss = np.array([0, 0, 12, 21, 42, 69])                # update
Desk_1024_dpdk = np.array([])

Desk_64_rdma = np.array([11.672, 23.287, 44.748, 72.742, 82.521])
Desk_128_rdma = np.array([])
Desk_256_rdma = np.array([])
eRPC_Desk_512_rdma = np.array([9.507, 17.717, 28.184, 20.629, 23.65])          # update #16
LineFS_Desk_512_rdma = np.array([0, 0, 14.482, 18.718, 17.972, 16.262])                         # update #1/2/4/8/12/16
LineFS_Desk_512_rdma_cache_miss = np.array([0, 23, 54, 63, 84, 91])              
Desk_1024_rdma = np.array([])

# P50 P99 P99.9
Desk_64_dpdk_lat_c16 = np.array([])
Desk_128_dpdk_lat_c16 = np.array([])
Desk_256_dpdk_lat_c16 = np.array([])
Desk_512_dpdk_lat_c1 = np.array([17.9, 20.3, 26.4])
Desk_512_dpdk_lat_c2 = np.array([18.65, 20.85, 24.95])
Desk_512_dpdk_lat_c4 = np.array([21.5, 25.65, 31.6])
Desk_512_dpdk_lat_c8 = np.array([29.962, 36.125, 45.487])
eRPC_Desk_512_dpdk_lat_c16 = np.array([97.1, 116.6, 126.8])     # update
OvS_Desk_512_dpdk_lat_c16 = np.array([0, 0, 0])                 # todo
LineFS_Desk_512_dpdk_lat_c16 = np.array([0, 0, 0])              # todo
Desk_1024_dpdk_lat_c16 = np.array([])

Desk_64_rdma_lat_c16 = np.array([])
Desk_128_rdma_lat_c16 = np.array([])
Desk_256_rdma_lat_c16 = np.array([])
Desk_512_rdma_lat_c1 = np.array([14.5, 15.4, 19.4])
Desk_512_rdma_lat_c2 = np.array([14.9, 16.2, 20.8])
Desk_512_rdma_lat_c4 = np.array([18.15, 21.25, 26.18])
Desk_512_rdma_lat_c8 = np.array([32.64, 42.55, 59])
eRPC_Desk_512_rdma_lat_c16 = np.array([72.5, 112.6, 219.85])  # update
OvS_Desk_512_rdma_lat_c16 = np.array([0, 0, 0])               # todo
LineFS_Desk_512_rdma_lat_c16 = np.array([0, 0, 0])             # todo
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
fig, ax = plt.subplots(figsize=(8, 2.5))    # ax: throughput
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
white = '#FFFFFF'  # white
pattern_1 = '\\\\'
pattern_2 = '//'
pattern_3 = '-.-.'
if branch == 'hardware_changes':
    colomn_width = 0.16
elif branch == 'LineFS':
    colomn_width = 0.11
colomn_gap = 0.06
group_gap = 0.1

# -----------------------Branch 3: core allocation-----------------------
if branch == 'LineFS':
    scale = 0.8
    x_labels = ['eRPC DPDK', 'eRPC RDMA', 'LineFS', 'dperf']

    colomn_num_per_label = 4    # throughput of 4/8/12/16 cores
    label_ticks = np.array(range(len(x_labels))) + (colomn_width + colomn_gap) * (colomn_num_per_label - 1) / 2
    for i in range(len(label_ticks)):
        label_ticks[i] = label_ticks[i] + i * group_gap

    first_colomn_tick = label_ticks - (colomn_width + colomn_gap) * (colomn_num_per_label - 1) / 2

    # draw throughput colomns
    max_tap_group = np.array([50, 50, 50, 50])
    ## draw eRPC throughput colomns
    eRPC_ticks = first_colomn_tick[0] + (colomn_width + colomn_gap) * np.array([0, 1, 2, 3])
    rects1_line_rate = ax.bar(eRPC_ticks, max_tap_group * scale, color=white, width=colomn_width, edgecolor=black_dark, linestyle='dashed', linewidth=1)
    tp_group = np.array([19.4, 30.7, 33.73, 34.4])
    rects1 = ax.bar(eRPC_ticks, tp_group * scale, color=blue, width=colomn_width, edgecolor=black, label='Thrpt')


    ## draw OvS throughput colomns
    OvS_ticks = first_colomn_tick[1] + (colomn_width + colomn_gap) * np.array([0, 1, 2, 3])
    rects2_line_rate = ax.bar(OvS_ticks, max_tap_group * scale, color=white, width=colomn_width, edgecolor=black_dark, linestyle='dashed', linewidth=1)
    tp_group = np.array([OvS_Desk_512_dpdk[2], OvS_Desk_512_dpdk[3], OvS_Desk_512_dpdk[4], OvS_Desk_512_dpdk[5]])
    rects2 = ax.bar(OvS_ticks, tp_group * scale, color=blue, width=colomn_width, edgecolor=black)



    ## draw LineFS throughput colomns
    LineFS_ticks = first_colomn_tick[2] + (colomn_width + colomn_gap) * np.array([0, 1, 2, 3])
    rects3_line_rate = ax.bar(LineFS_ticks, max_tap_group * scale, color=white, width=colomn_width, edgecolor=black_dark, linestyle='dashed', linewidth=1)
    tp_group = np.array([LineFS_Desk_512_rdma[2], LineFS_Desk_512_rdma[3], LineFS_Desk_512_rdma[4], LineFS_Desk_512_rdma[5]])
    rects3 = ax.bar(LineFS_ticks, tp_group * scale, color=blue, width=colomn_width, edgecolor=black)


 




    ## 添加ACCLIO的柱状图
    ACCLIO_ticks = first_colomn_tick[3] + (colomn_width + colomn_gap) * np.array([0, 1, 2, 3])
    rects4_line_rate = ax.bar(ACCLIO_ticks, max_tap_group * scale, color=white, width=colomn_width, edgecolor=black_dark, linestyle='dashed', linewidth=1)
    # 请替换为ACCLIO的实际数据
    tp_group = np.array([20.0, 32.0, 35.0, 36.0])  # 示例数据，请替换
    rects4 = ax.bar(ACCLIO_ticks, tp_group * scale, color=blue, width=colomn_width, edgecolor=black)



  # 更新minor ticks
    labels_minor = ['128B', '256B', '512B', '1024B', '128B', '256B', '512B', '1024B', '128B', '256B', '512B', '1024B', '128B', '256B', '512B', '1024B']
    labels_minor_ticks = np.concatenate([eRPC_ticks, OvS_ticks, LineFS_ticks, ACCLIO_ticks])

    y_lable = ["0", "10", "20", "30", "40", "50"]
    y_tick = np.array([0, 10, 20, 30, 40, 50]) * scale
    ax.set_yticks(y_tick)
    ax.set_yticklabels(y_lable, fontsize=y_label_size)


    # Configure axes
    ax.set_xticks(label_ticks)
    ax.set_xticklabels(x_labels, fontsize=x_label_size)
    
    # Minor ticks for packet sizes
    labels_minor = ['128B', '256B', '512B', '1024B'] * len(x_labels)
    labels_minor_ticks = np.concatenate([eRPC_ticks, OvS_ticks, LineFS_ticks, ACCLIO_ticks])
    ax.set_xticks(labels_minor_ticks, minor=True)
    ax.set_xticklabels(labels_minor, minor=True, rotation=45)  # Added rotation=45
    
    # Styling
    ax.tick_params(axis='x', which='minor', length=0, labelsize=x_label_size-4, pad=8)  # Increased padding to 8
    ax.tick_params(axis='x', which='major', length=12, width=0, labelsize=x_label_size, pad=20)
    

    for label in ax.get_xticklabels(which='major'):
        label.set_y(-0.02) 

    ax.set_ylabel('Throughput (Mpps)', fontsize=title_size, fontweight='bold')




# -----------------------Output-----------------------
if output == 'show':
    plt.show()
else:
    print(branch+'.pdf')
    output_path = '/Users/bowen/Documents/HKUST/acclio/paper/ACCLIO/figs/evaluation/'  # 修改为你的实际路径
    plt.savefig(output_path + 'micro_throughput' + '.pdf', bbox_inches='tight')