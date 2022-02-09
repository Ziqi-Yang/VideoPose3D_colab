import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

keypoints_npz_path = "./data/前后摇摆_0.npy"
DATA = np.load(keypoints_npz_path)

# matplotlib.use("agg") # 不显示控制窗口
# plt.ioff() # 禁止交互式
fig = plt.figure(figsize=(12,10))
ax = fig.add_subplot(projection="3d")

coord_scale = []
for i in range(3):
    tmp = [DATA[:,:,i].min() - abs(DATA[:,:,i].min())*0.1, DATA[:,:,i].max() + abs(DATA[:,:,i].max()) * 0.1]
    coord_scale.append(tmp)


ax.set_xlim3d(*coord_scale[0])
ax.set_ylim3d(*coord_scale[1])
ax.set_zlim3d(*coord_scale[2])


ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_zticklabels([])
ax.view_init(-87,-90)

draw_sequences = np.array([ # 人体骨骼框架连线
    [0,1,2,3],
    [0,4,5,6],
    [0,7,8,9,10],
    [8,11,12,13],
    [8,14,15,16]
    ],dtype=object)


lines = [ax.plot([],[],[],c="steelblue",marker="o")[0] for _ in range(len(draw_sequences))]

def update(keyPoints):

    index = 0
    for seq in draw_sequences:
        Vertexes = np.array([keyPoints[i] for i in seq]).T

        lines[index].set_data(Vertexes[:2,:])
        lines[index].set_3d_properties(Vertexes[2,:])
        index += 1



anim = animation.FuncAnimation(fig,update,DATA,interval=40) # 在interval处修改美帧间隔时间
anim.save("res.mp4",dpi=300)
