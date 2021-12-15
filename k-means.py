import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import copy

x = [2, 4, 6, 10, 12, 14]
y = [0, 0, 0, 0, 0, 0]
c = [0, 5] #クラスタの中央の座標

count = [0] #試行回数をカウントする用の変数
z_new = [0, 0, 0, 0, 0, 0]  # 各点の状態を保存。０ならc1に近い、１ならc2に近い
z_past = [2, 2, 2, 2, 2, 2]  # 過去の点の状態を記憶する箱(初期値は2、比較用）
c_data = [] #秒数ごとのｃのデータ一覧
z_data = [] #秒数ごとのｚのデータ一覧
fig = plt.figure()
ax = fig.add_subplot(111)

def k_means():
    #k-means法を行う
    while z_new != z_past:
        c_data.append(copy.deepcopy(c)) #Cのデータを一覧に格納
        for i in range(len(z_new)):  # 最新の状態を過去の状態にコピーする
            z_past[i] = z_new[i]
        c1 = []
        c2 = []
        # それぞれのｃとｘの距離を比べる
        for i in range(len(x)):
            for j in range(len(c)):
                if j == 0:  # 最初はｘはｃ１に近い点だと仮定する
                    z_new[i] = 0
                    e = abs(abs(x[i]-c[j])**2)  # eにxとcの距離を代入
                elif e > (abs(x[i]-c[j])**2):  # もしeがｃ２とｘの距離より大きかったらzの値を更新
                    z_new[i] = j
        z_data.append(copy.deepcopy(z_new))

        # xがc1とc2のどちらに属しているか判定する
        for k in range(len(x)):
            if z_new[k] == 0:
                c1.append(x[k])
            else:
                c2.append(x[k])

        # cの値を属しているxの平均値に再計算する
        c[0] = np.mean(c1)
        c[1] = np.mean(c2)
        count[0] += 1

    #アニメーションを作る
    ani = FuncAnimation(fig, k_means_plot, frames = count[0],interval=1000)

    plt.show()
    ani.save("kmeans.gif", writer="Imagemagick")


def k_means_plot(frame):
    ax.cla()
    for l in range(len(x)):
        if z_data[frame][l] == 0:  # c1に属しているなら赤
            ax.plot(x[l], y[l], marker=".", color="red")
        elif z_data[frame][l] == 1:  # c2に属しているなら青
            ax.plot(x[l], y[l], marker=".", color="blue")
        ax.plot(c_data[frame][0], y[l]+1, marker=".", color="black")  # c1は黒
        ax.plot(c_data[frame][1], y[l]+1, marker=".", color="green")  # c2は緑

k_means()