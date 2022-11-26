import numpy as np
import matplotlib.pyplot as plt
import random

e=-100
#A,B,C,E,F,G,H,I
#行けるときは報酬の値を、行けないときは-1
reward = np.array([[2,1,0,e,e,e,e,e], #SからはABCに行ける
                 [e,e,e,e,e,0,-1,e], #AからはG,Hに行ける
                 [e,0,e,e,e,e,e,e], #BからはBに行ける
                 [e,e,e,3,1,e,e,e], #CからはE,Fに行ける
                 [e,e,e,0,e,e,e,e], #EからはEに行ける
                 [e,e,e,e,e,e,e,-1], #FからはIにいける
                 [e,e,e,e,e,0,e,e], #GからはGに行ける
                 [e,e,e,e,e,e,0,e]]) #HからはHに行ける
num_episode=3000
alpha=0.1
gamma=0.9
epsilon=0.05
t=3 #3回繰り返したら終了
date=[]
rewards=[]

def Qlearning():
    Q = np.array(np.zeros([9,8]))

    for i in range(0,num_episode):#1万回繰り返し学習を行う
        p_state = 0 #現在の状態をランダムに選択
        episode_reward=[]
        for k in range(t):
            n_actions = []#次の行動の候補を入れる箱
            for j in range(8):
                if reward[p_state,j] != e:#rewardの各行が1以上のインデックスを取得
                    n_actions.append(j)#これでp_stateの状態で移動できる場所を取得
            if np.random.rand() < epsilon:
                n_state = np.random.choice(n_actions) #行動可能選択肢からランダムに選択
            else: # greedy行動
                n_state = n_actions[0]
                for l in range(len(n_actions)):
                    if Q[p_state,n_actions[l]]>Q[p_state,n_state]:
                        n_state = n_actions[l]
            #Q値の更新。学習率が小さいほど現在の行動価値が重視され、更新がゆるやかとなる
            #ここでQ学習に用いる「たった一つの数式」を利用して行動価値を学習していく
            Q[p_state,n_state] = (1-alpha)*Q[p_state,n_state]+alpha*(reward[p_state,n_state]+gamma*Q[n_state+1,np.argmax(Q[n_state+1,])])
            episode_reward.append(reward[p_state,n_state])
            p_state = n_state+1
        rewards.append(np.sum(episode_reward))
    print(Q)
Qlearning()

n=50
x = [n*i+n for i in range(int(num_episode/n))]
y = []
print(len(y))
for i in range(int(num_episode/n)):
    y_hub=[]
    for j in range(n):
        y_hub.append(rewards[i*n+j])
    print(y_hub)
    print(y)
    y.append(np.mean(y_hub))

plt.plot(x, y , linewidth=0.7)
plt.xlabel("episode")
plt.ylabel("reward")
plt.savefig("result.jpg")
plt.show()