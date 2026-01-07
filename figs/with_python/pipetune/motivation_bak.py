import matplotlib.pyplot as plt
import numpy as np

branch = 'latency' # ['hardware_changes', 'workload_changes', 'latency']
output = 'show' # ['show', 'save'] 

# -----------------------source data in eRPC echo mode-----------------------
# TACC
TACC_64_dpdk = np.array([2.066, 3.969, 7.789, 14.584, 23.413])
TACC_128_dpdk = np.array([])
TACC_256_dpdk = np.array([])
TACC_512_dpdk = np.array([5.412, 8.899, 13.779, 17.91, 17.724])
TACC_1024_dpdk = np.array([])

TACC_64_rdma = np.array([1.444, 2.782, 5.406, 9.889, 17.005])
TACC_128_rdma = np.array([])
TACC_256_rdma = np.array([])
TACC_512_rdma = np.array([1.424, 2.618, 4.645, 7.885, 12.474])
TACC_1024_rdma = np.array([])

# Desktop
Desk_64_dpdk = np.array([7.916, 15.404, 29.652, 40.685, 37.095])
Desk_128_dpdk = np.array([])
Desk_256_dpdk = np.array([])
Desk_512_dpdk = np.array([7.542, 14.059, 24.845, 35.932, 31.262])
Desk_1024_dpdk = np.array([])

Desk_64_rdma = np.array([11.672, 23.287, 44.748, 72.742, 82.521])
Desk_128_rdma = np.array([])
Desk_256_rdma = np.array([])
Desk_512_rdma = np.array([9.507, 17.717, 28.184, 20.629, 27.726])
Desk_1024_rdma = np.array([])

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
fig, ax = plt.subplots(figsize=(6, 2.5))
orange = '#FE6331'  # orange
orange_dark = '#BF4B25'  # orange_dark
gray = '#E9E2EA'  # gray
gray_dark = '#848085'  # gray_dark
black = '#282D32'  # black
black_dark = '#000000'  # black_dark
white = '#FFFFFF'  # white
colomn_width = 0.1
colomn_gap = 0.05
# -----------------------Branch 1: hardware_changes-----------------------
if branch == 'hardware_changes':
    scale = 0.8
    x_labels = ['1', '2', '4', '8', '16']
    label_ticks = range(len(x_labels))
    ax.set_xticks(label_ticks)
    ax.set_xticklabels(x_labels)

    colomn_num_per_label = 4
    first_colomn_tick = np.array(range(len(x_labels))) - (colomn_width + colomn_gap) * (colomn_num_per_label - 1) / 2

    # draw colomns
    rects1 = ax.bar(first_colomn_tick, TACC_512_dpdk * scale, color=orange, width=colomn_width, edgecolor=orange_dark)
    rects2 = ax.bar(first_colomn_tick + colomn_width + colomn_gap, TACC_512_rdma * scale, color=gray, width=colomn_width, edgecolor=gray_dark)
    rects3 = ax.bar(first_colomn_tick + 2 * (colomn_width + colomn_gap), Desk_512_dpdk * scale, color=black, width=colomn_width, edgecolor=black_dark)
    rects4 = ax.bar(first_colomn_tick + 3 * (colomn_width + colomn_gap), Desk_512_rdma * scale, color=white, width=colomn_width, edgecolor=black_dark)

    # draw 100G and 200G line
    ax.axhline(y=25*scale, color='black', linestyle='--', linewidth=1)
    plt.text(-0.4, 22*scale, '100Gbps', fontsize=8, fontweight='bold')
    ax.axhline(y=50*scale, color='black', linestyle='--', linewidth=1)
    plt.text(-0.4, 47*scale, '200Gbps', fontsize=8, fontweight='bold')

    # draw line for TACC_512_rdma
    ax.plot(first_colomn_tick + 3 * (colomn_width + colomn_gap), Desk_512_rdma * scale, marker='o', markersize=3, color=orange_dark)

    # draw legend
    plt.legend([rects1, rects2, rects3, rects4], ['100G-server w/o RDMA', '100G-server with RDMA', '200G-server w/o RDMA', '200G-server with RDMA'], fontsize=10, ncol=2, frameon = True, bbox_to_anchor=(0.07, 1.01), loc=3, borderaxespad=0)

    ax.set_ylabel('Throughput (Mrps)', fontsize=12, fontweight='bold')
    ax.set_xlabel('Parallism (Core Number)', fontsize=12, fontweight='bold')

    y_lable = ["0", "10", "20", "30", "40", "50"]
    y_tick = np.array([0, 10, 20, 30, 40, 50]) * scale
    ax.set_yticks(y_tick)
    ax.set_yticklabels(y_lable)

# -----------------------Branch 2: workload_changes-----------------------
elif branch == 'workload_changes':
    scale = 0.8
    x_labels = ['64B', '128B', '256B', '512B', '1024B']

    colomn_num_per_label = 1
    first_colomn_tick = np.array(range(len(x_labels))) - (colomn_width + colomn_gap) * (colomn_num_per_label - 1) / 2

    # draw boxs
    boxes = ax.boxplot([DThub_64_lat_c1, DThub_128_lat_c1, DThub_256_lat_c1, DThub_512_lat_c1, DThub_1024_lat_c1], labels=x_labels, positions=first_colomn_tick, widths=colomn_width, patch_artist=True, boxprops=dict(facecolor=orange, color=orange_dark), whiskerprops=dict(color=black), capprops=dict(color=black), medianprops=dict(color=black_dark))

    # draw line for median
    medians = [item.get_ydata()[0] for item in boxes['medians']]
    x_pos = np.arange(len(medians))
    plt.plot(x_pos, medians, marker='o', markersize=1, linestyle='-', color=black)

    ax.set_ylabel('Latency ' + r'$\mu$s', fontsize=12, fontweight='bold')
    ax.set_xlabel('RPC size', fontsize=12, fontweight='bold')

# -----------------------Branch 3: latency-----------------------

# -----------------------Output-----------------------
if output == 'show':
    plt.show()
else:
    plt.savefig(branch+'.pdf', bbox_inches='tight')