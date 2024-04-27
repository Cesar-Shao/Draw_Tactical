import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
from matplotlib.lines import Line2D

def get_res(seqcond_,seq_):
    for i in range(seq_.shape[0]):
        for j in range(seq_.shape[1]):
            if np.count_nonzero(1) == 1:
                # 获取元素为 1 的索引
                location_1 = np.where(seqcond_[i, j] == 1)[0]
                if not location_1.size == 0:
                    if not location_1[0] == 5:
                        index = location_1[0]
                # print("1 的位置是:", index)
                    seq_[i, j, 0] = seq_[i, j, index]
    return seq_

# 载入数据
seqcond = np.load('BasketballGAN-master/data/RealCond.npy')
seq = np.load('BasketballGAN-master/data/50Real.npy')
seq = seq[:,:,:6,:2]
data = seq[1,:,:]
seqcond=seqcond[1,:,:]

# 提取球员和球的坐标数据
player_data = data[:,1:,:].reshape(50, 5, 2)
ball_data = data[:,:1,:].reshape(50, 2)

# 创建图形对象
fig, ax = plt.subplots(figsize=(6, 6))  # 调整图形对象的大小

# 载入篮球场地背景图像
court_img = plt.imread('BasketballGAN-master/data/court.png')
height=court_img.shape[0]*0.1
width=court_img.shape[1]*0.1
ax.imshow(court_img, extent=[0,width,0,height])

# 创建空的轨迹容器
player_trajectories = [[] for _ in range(5)]
handler_trajectories=[]
ball_trajectory = []

# 绘制球员和球的初始位置
players = ax.scatter([], [], color='black', label='Player')
ball = ax.scatter([], [], color='orange', label='Ball')
handler = ax.scatter([], [], color='red', label='Handler')

# 绘制轨迹
player_lines = [ax.plot([], [], color='black')[0] for _ in range(5)]
ball_line = ax.plot([], [], color='orange')[0]
#ball_line = Line2D([], [], linestyle='--', color='orange')
handler_line = ax.plot([], [], color='red')[0]

# 设置图例和标题
ax.legend()
ax.set_title('Player and Ball Animation')

# 设置坐标轴范围
ax.set_xlim(0,width)
ax.set_ylim(0,height)

# 更新函数，用于每一帧的绘制

'''def update(frame):
    # 更新球员和球的位置
    players.set_offsets(player_data[frame])
    ball.set_offsets(ball_data[frame])
    handler = np.where(seqcond[frame] == 1)[0]
    
    # 更新球员的轨迹
    for i in range(5):
        if not len(handler) == 0:
            if i == handler[0]:
                handler_trajectories.append(player_data[frame, i])
                player_trajectories[i].append(np.array([None,None]))
            else:
                # 如果不是持球球员，更新其他球员的轨迹
                player_trajectories[i].append(player_data[frame, i])
        else:        
            # 如果没有持球球员，更新所有球员的轨迹
            player_trajectories[i].append(player_data[frame, i])
            handler_trajectories.append(np.array([None,None]))
            ball_trajectory.append(ball_data[frame])


    # 更新持球球员的轨迹线
    x_values = [coord[0] for coord in handler_trajectories]
    y_values = [coord[1] for coord in handler_trajectories]
    handler_line.set_data(x_values, y_values)

    # 更新其他球员的轨迹线
    for i in range(5):
        if not len(handler) == 0 and i == handler[0]:
            # 如果是持球球员，跳过绘制轨迹线
            continue
        else:
            x_values = [coord[0] for coord in player_trajectories[i]]
            y_values = [coord[1] for coord in player_trajectories[i]]
            player_lines[i].set_data(x_values, y_values)

    # 更新球的轨迹
    ball_trajectory.append(ball_data[frame])
    x_values = [coord[0] for coord in ball_trajectory]
    y_values = [coord[1] for coord in ball_trajectory]
    ball_line.set_data(x_values, y_values)
    ball_line.set_linestyle('--')'''

def update(frame):
    # 更新球员和球的位置
    players.set_offsets(player_data[frame])
    ball.set_offsets(ball_data[frame])
    handler = np.where(seqcond[frame] == 1)[0]
    
    # 更新球员的轨迹
    for i in range(5):
        if not len(handler) == 0:
            if i == handler[0]:
                handler_trajectories.append(player_data[frame, i])
                player_trajectories[i].append(np.array([None, None]))
            else:
                # 如果不是持球球员，更新其他球员的轨迹
                player_trajectories[i].append(player_data[frame, i])
                # 绘制其他球员的轨迹线
                x_values = [coord[0] for coord in player_trajectories[i]]
                y_values = [coord[1] for coord in player_trajectories[i]]
                player_lines[i].set_data(x_values, y_values)
        else:
            # 如果没有持球球员，更新所有球员的轨迹
            player_trajectories[i].append(player_data[frame, i])
            handler_trajectories.append(np.array([None, None]))
            # 绘制所有球员的轨迹线
            x_values = [coord[0] for coord in player_trajectories[i]]
            y_values = [coord[1] for coord in player_trajectories[i]]
            player_lines[i].set_data(x_values, y_values)

    # 更新持球球员的轨迹线
    x_values = [coord[0] for coord in handler_trajectories]
    y_values = [coord[1] for coord in handler_trajectories]
    handler_line.set_data(x_values, y_values)

    # 更新球的轨迹
    if len(handler) == 0:  # 没有持球球员时绘制球的轨迹
        ball_trajectory.append(ball_data[frame])
        x_values = [coord[0] for coord in ball_trajectory]
        y_values = [coord[1] for coord in ball_trajectory]
        ball_line.set_data(x_values, y_values)
        ball_line.set_linestyle('--')
    else:
        ball_trajectory.append(np.array([None, None]))
    print(ball_trajectory)
    print('------------------------')

# 创建动画
animation = FuncAnimation(fig, update, frames=range(50), interval=200)

# 创建写入器
writer = FFMpegWriter(fps=10)

# 保存动画为视频文件
animation.save('animation.mp4', writer=writer)

# 显示动画
plt.show()