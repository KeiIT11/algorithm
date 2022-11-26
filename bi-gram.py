inf_minus = -float('inf')
def DP (data_set, name_set, T):
    F = [[[inf_minus] * 3 for i in range(T)] for k in range(2)]

    #マスが最大値をとるとき、どのマスから来たか記録する変数
    prev_x=[[0] * 3 for i in range(T)]
    prev_y=[[0] * 3 for i in range(T)]

    max_name = ["AA" for i in range(T)] #最大値をとるマスの名前を記録する変数

    for m in range(3):
        for l in range(T):
             F[1][l][m] = name_set[m][l]
             #メモ[深さ][長さ][高さ]

    #動的計画法を実行
    for t in range(T):
        if t == 0:
            for i in range(3):
                F[0][0][i] = 0

        elif t == 1:
            for i in range(3):
                if (F[0][t-1][i] + data_set[t-1][i]) >= F[0][t][i]:
                    F[0][t][i] = F[0][t-1][i] + data_set[t-1][i]
                    prev_x[t][i]=t-1
                    prev_y[t][i]=i

        elif t == T-1:
            for i in range(3):
                if (F[0][t-1][i] + data_set[t-1][i]) >= F[0][t][i]:
                    F[0][t][i] =  F[0][t-1][i] + data_set[t-1][i]
                    prev_x[t][i]=t-1
                    prev_y[t][i]=i

        else:
            if (F[0][t-1][0] + data_set[t-1][0]) >= F[0][t][0]:
                F[0][t][0] = F[0][t-1][0] + data_set[t-1][0]
                prev_x[t][0]=t-1
                prev_y[t][0]=0

            if (F[0][t-1][0] + data_set[t-1][1]) >= F[0][t][1]:
                F[0][t][0] = F[0][t-1][1] + data_set[t-1][1]
                prev_x[t][0]=t-1
                prev_y[t][0]=1

            if (F[0][t-1][1] + data_set[t-1][2]) >= F[0][t][1]:
                F[0][t][1] = F[0][t-1][1] + data_set[t-1][2]
                prev_x[t][1]=t-1
                prev_y[t][1]=1

            if (F[0][t-1][2] + data_set[t-1][4]) >= F[0][t][1]:
                F[0][t][1] = F[0][t-1][2] + data_set[t-1][4]
                prev_x[t][1]=t-1
                prev_y[t][1]=2

            if (F[0][t-1][1] + data_set[t-1][3]) >= F[0][t][2]:
                F[0][t][2] = F[0][t-1][1] + data_set[t-1][3]
                prev_x[t][2]=t-1
                prev_y[t][2]=1

    #最適経路を求める
    list = [F[0][T-1][0],F[0][T-1][1],F[0][T-1][2]] #maxのインデックスを取得するために使う変数
    max_x = T-1
    max_y = list.index(max(list))
    max_name[T-1] = F[1][T-1][list.index(max(list))]

    for t in range(1,T):
        max_y = prev_y[max_x][max_y]
        max_x = prev_x[max_x][max_y]

        max_name[int(T-t-1)] = F[1][int(max_x)][int(max_y)]

    #経路の最大値を表示
    print("最大値は",max(F[0][T-1][0],F[0][T-1][1],F[0][T-1][2]))
    #最大値をとる経路を表示
    print("最大値をとる経路は",max_name)

def main():
    data_set = [[2,5,4],[-5,3,2,3,5],[3,1,-2,2,0],[4,4,2,7,0],[2,1,8]]
    name_set = [["り","ん","め","い","か","ん"],["り","つ","い","あ","と","ん"],["り","ば","う","い","さ","ん"]]
    T = len(data_set)+1
    DP(data_set, name_set, T)

main()