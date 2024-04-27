#realcon & real50
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter

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
                    seq_[i,j,0]=seq_[i,j,index]
    return seq_


seqcond=np.load('/Users/cesar/Library/Mobile Documents/com~apple~CloudDocs/Desktop/同步储存/Sports Analytics/hoop_transformer/BasketballGAN-master/data/RealCond.npy')
seq=np.load('/Users/cesar/Library/Mobile Documents/com~apple~CloudDocs/Desktop/同步储存/Sports Analytics/hoop_transformer/BasketballGAN-master/data/50Real.npy')
seq=seq[:,:,:6,:2]
# 创建数据（示例数据）
#data=get_res(seqcond[:10,:,:],seq[:10,:,:])
data=seq[1,:,:]

print(data)
print(data[:,2:,:].shape)

ball = seqcond[1,:,:5]  # 替换为您的 50x5 持球人数组
handler_data=[[]]

for i in range(ball.shape[1]):
    print(type(ball[i]))

# 提取球员和球的坐标数据
player_data = data[:,1:,:].reshape(50, 5, 2)
ball_data = data[:,:1,:].reshape(50, 2)

# 创建图形对象
fig, ax = plt.subplots()

# 创建空的轨迹容器
player_trajectories = [[] for _ in range(5)]
ball_trajectory = []

# 绘制球员和球的初始位置
players = ax.scatter([], [], color='black', label='Player')
ball = ax.scatter([], [], color='orange', label='Ball')
handler = ax.scatter([], [], color='red', label='Handler')

# 绘制轨迹
player_lines = [ax.plot([], [], color='black')[0] for _ in range(5)]
ball_line = ax.plot([], [], color='orange')[0]
handler_line=ax.plot([],[],color='red')[0]

# 设置图例和标题
ax.legend()
ax.set_title('Player and Ball Animation')

# 设置坐标轴范围
ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)

# 更新函数，用于每一帧的绘制
def update(frame):
    # 更新球员和球的位置
    players.set_offsets(player_data[frame])
    ball.set_offsets(ball_data[frame])

    # 更新球员的轨迹
    for i in range(5):
        player_trajectories[i].append(player_data[frame, i])
        x_values = [coord[0] for coord in player_trajectories[i]]
        y_values = [coord[1] for coord in player_trajectories[i]]
        player_lines[i].set_data(x_values, y_values)

    # 更新球的轨迹
    ball_trajectory.append(ball_data[frame])
    x_values = [coord[0] for coord in ball_trajectory]
    y_values = [coord[1] for coord in ball_trajectory]
    ball_line.set_data(x_values, y_values)

# 创建动画
animation = FuncAnimation(fig, update, frames=range(50), interval=200)

# 创建写入器
writer = FFMpegWriter(fps=10)

# 保存动画为视频文件
animation.save('animation.mp4', writer=writer)

# 显示动画
plt.show()