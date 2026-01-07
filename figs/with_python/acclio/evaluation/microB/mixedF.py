import matplotlib.pyplot as plt



branch = 'mixedF' 
output = 'show' # ['show', 'save'] 


# 创建空白图片
fig, ax = plt.subplots(figsize=(8, 2.5))

# 隐藏所有轴线和刻度
ax.axis('off')






# -----------------------Output-----------------------
if  output == 'show':
    plt.show()
else:
    print(branch+'.pdf')
    output_path = '/Users/bowen/Documents/HKUST/acclio/paper/ACCLIO/figs/evaluation/'  # 修改为你的实际路径
    plt.savefig(output_path + 'mixedF' + '.pdf', bbox_inches='tight')
