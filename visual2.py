import matplotlib.pyplot as plt
import numpy as np




def get_res(seqcond_,seq_):

    for i in range (seq_.shape[0]):
        for j in range(seq_.shape[1]):
            if np.count_nonzero(1) == 1:
                # 获取元素为 1 的索引
                location_1=np.where(seqcond_[i,j]==1)[0]
                if not location_1.size==0 :
                    if not location_1[0]==5 :
                        index = location_1[0]
                #print("1 的位置是:", index)
                    seq_[i,j,-3:-1]=seq_[i,j,index*2:index*2+2]
    return seq_


seqcond=np.load('/Users/cesar/Library/Mobile Documents/com~apple~CloudDocs/Desktop/同步储存/Sports Analytics/hoop_transformer/BasketballGAN-master/data/SeqCond.npy')
seq=np.load('/Users/cesar/Library/Mobile Documents/com~apple~CloudDocs/Desktop/同步储存/Sports Analytics/hoop_transformer/BasketballGAN-master/data/50Seq.npy')
data=get_res(seqcond[:10,:,:],seq[:10,:,:])




# 定义数据
player_data = data[:10,:,:10]*40  # 球员坐标数据
ball_data = data[:10,:,-2:]*40  # 球的坐标数据

print(player_data[1,1,:])
print(ball_data[1,1,:])
# 创建图形对象
fig, ax = plt.subplots()

# 绘制球员轨迹
colors = ['r', 'g', 'b', 'c', 'm']  # 每名球员的颜色
for player_id in range(5):
    player_trajectory = player_data[player_id]
    x_values = [coord[0] for coord in player_trajectory]
    y_values = [coord[1] for coord in player_trajectory]
    ax.plot(x_values, y_values, color=colors[player_id], label=f'Player {player_id+1}')

# 绘制球的轨迹
ball_x = [coord[0] for coord in ball_data]
ball_y = [coord[1] for coord in ball_data]
ax.plot(ball_x, ball_y, color='k', linestyle='--', label='Ball')

# 设置图例和标题
ax.legend()
ax.set_title('Player and Ball Trajectories')

# 设置坐标轴范围
ax.set_xlim(-100, 100)  # 根据实际情况调整坐标轴范围
ax.set_ylim(-100, 100)  # 根据实际情况调整坐标轴范围

# 去除坐标轴刻度
ax.set_xticks([])
ax.set_yticks([])

# 去除边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

# 显示图像
plt.show()



'''
# 绘制球场背景
court_img = plt.imread('BasketballGAN-master/data/court.png')
fig, ax = plt.subplots()
ax.imshow(court_img)
# 绘制球员轨迹
colors = ['r', 'g', 'b', 'c', 'm']  # 每名球员的颜色
for player_id in range(5):
    player_trajectory = player_data[player_id]
    x_values = [coord[0] for coord in player_trajectory]
    y_values = [coord[1] for coord in player_trajectory]
    ax.plot(x_values, y_values, color=colors[player_id], label=f'Player {player_id+1}')

# 绘制球的轨迹
ball_x = [coord[0] for coord in ball_data]
ball_y = [coord[1] for coord in ball_data]
ax.plot(ball_x, ball_y, color='k', linestyle='--', label='Ball')

# 设置图例和标题
ax.legend()
ax.set_title('Player and Ball Trajectories')

# 显示图像
plt.show()'''