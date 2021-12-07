import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import copy

x = [2, 4, 6, 10, 12, 14]
y = [0, 0, 0, 0, 0, 0]
c = [0, 5]
count = [0]
z_new = [0, 0, 0, 0, 0, 0]  # 各点の状態、０ならc1に近い、１ならc2に近い
z_past = [2, 2, 2, 2, 2, 2]  # 過去の点の状態を記憶する箱(初期値は2)


def k_means(c, z_past, z_new,count):
    ims = []
    while z_new != z_past:
        k_means_calc(c, z_past, z_new)

    #使った値を初期化する
    x = [2, 4, 6, 10, 12, 14]
    y = [0, 0, 0, 0, 0, 0]
    c = [0, 5]
    count = [0]
    z_new = [0, 0, 0, 0, 0, 0]  # 各点の状態、０ならc1に近い、１ならc2に近い
    z_past = [2, 2, 2, 2, 2, 2]

    print(x)
    print(y)
    print(c)
    print(count)
    print(z_new)
    print(z_past)

    """
    #グラフをプロットする
    while z_new != z_past:
        k_means_calc(c, z_past, z_new)
    """

def k_means_calc(c, z_past, z_new):
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

def k_means_plot():
    fig, ax = plt.subplots()
    for l in range(len(x)):
        if z_new[l] == 0:  # c1に属しているなら赤
            im = ax.plot(x[l], y[l], marker=".", color="red")
        elif z_new[l] == 1:  # c2に属しているなら青
            im = ax.plot(x[l], y[l], marker=".", color="blue")
        im = ax.plot(c[0], y[l]+1, marker=".", color="black")  # c1は黒
        im = ax.plot(c[1], y[l]+1, marker=".", color="green")  # c2は緑
        ims.append(im)

    ani = animation.ArtistAnimation(fig, ims, interval=1000)
    plt.show()
    ani.save("kmeans.gif", writer="Imagemagick")


k_means(c, z_past, z_new,count)
