import matplotlib.pyplot as plt
import numpy as np
from matplotlib import gridspec

branch = 'changeable' 
output = 'show' # ['show', 'save'] 

# -------changeable-------
erpc_desktop_changeable = np.array([48.1, 45.8, 35.2, 48.1, 38.4])
erpc_rdma_changeable = np.array([43.69, 42.8, 42.4, 43.69, 34.4])
LineFS_changeable = np.array([33.69, 32.8, 32.4, 33.69, 24.4])

# -----------------------Fig configuration-----------------------
plt.rcParams['font.sans-serif'] = 'Times'
if branch == 'changeable':
    fig, ax = plt.subplots(figsize=(8, 2.0))

x_label_size = 14
y_label_size = 14
legend_size = 13
title_size = 18
orange = '#FE6331'  # orange
orange_dark = '#BF4B25'  # orange_dark
gray = '#E9E2EA'  # gray
gray_dark = '#848085'  # gray_dark
black = '#282D32'  # black
black_dark = '#000000'  # black_dark
white = '#FFFFFF'  # white
pattern_1 = '\\\\'
pattern_2 = '//'
pattern_3 = '-.-.'

colomn_gap = 0.06
group_gap = 0.2

# -----------------------Draw the figure-----------------------

if branch == 'changeable':
    x_ticks = np.array(range(len(erpc_desktop_changeable) * 10)) 
    variation = 0.5

    # -------eRPC (DPDK)-------
    thrpt_values = []
    for avg_thrpt in erpc_desktop_changeable:
        for i in range(10):
            # add random variation
            thrpt_values.append(avg_thrpt + np.random.uniform(-variation, variation))
    line_real_thrpt = ax.plot(x_ticks, thrpt_values, marker='o', markersize=3, color=black, label='Optimzed eRPC (DPDK)')

    # -------eRPC (RDMA)-------
    thrpt_values = []
    for avg_thrpt in erpc_rdma_changeable:
        for i in range(10):
            # add random variation
            thrpt_values.append(avg_thrpt + np.random.uniform(-variation, variation))
    line_real_thrpt = ax.plot(x_ticks, thrpt_values, marker='o', markersize=3, color=orange_dark, label='Optimzed eRPC (RDMA)')

    # -------LineFS-------
    thrpt_values = []
    for avg_thrpt in LineFS_changeable:
        for i in range(10):
            # add random variation
            thrpt_values.append(avg_thrpt + np.random.uniform(-variation, variation))
    line_real_thrpt = ax.plot(x_ticks, thrpt_values, marker='o', markersize=3, color=gray_dark, label='LineFS')

    # -------add line and description for each 10s-------
    description = ['Apply\noptimized \nconfigs',
                   'Increase\nburst degree',
                   'Increase\nburst degree',
                   'Revert to \nstart point',
                   'Double \nRPC size']
    for i in range(5):
        line_tick = i * 10
        ax.plot([line_tick, line_tick], [0, 50], color=gray_dark, linestyle='dashed')
        ax.text(line_tick + 0.5, 1, description[i], fontsize=legend_size)

    # -------x-axis, y-axis, title, legend-------
    x_ticks = [0, 10, 20, 30, 40, 50]
    x_labels = ['0', '10', '20', '30', '40', '50']
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_labels, fontsize=x_label_size)

    y_lable = ["0", "10", "20", "30", "40", "50"]
    y_tick = np.array([0, 10, 20, 30, 40, 50])
    ax.set_yticks(y_tick)
    ax.set_yticklabels(y_lable, fontsize=y_label_size)

    # 获取图例handles和labels
    handles, labels = ax.get_legend_handles_labels()
    
    # 更新图例
    ax.legend(handles, labels, 
              fontsize=legend_size, 
              ncol=len(handles),  # 将所有图例排成一行
              frameon=False, 
              bbox_to_anchor=(0.5, 1.05),  # 调整位置到图片正上方
              loc='lower center', 
              borderaxespad=0.,
              handlelength=1.5, 
              handletextpad=0.4,
              columnspacing=1.5)  # 增加列间距

    ax.set_ylabel('Thrpt (Mpps)', fontsize=title_size)
    ax.set_xlabel('Time (s)', fontsize=title_size, fontweight='bold')


# -----------------------Output-----------------------
if output == 'show':
    plt.show()
else:
    print(branch+'.pdf')
    output_path = '/Users/bowen/Documents/HKUST/acclio/paper/ACCLIO/figs/evaluation/'  # 修改为你的实际路径
    plt.savefig(output_path + 'micro_degrade' + '.pdf', bbox_inches='tight')