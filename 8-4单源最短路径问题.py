

# -*- coding:utf-8 -*-
import sys

def sort_by_minedge(item):
    return item[2]

def Dijkstra(edges,points):

    if not points or len(points)<=0 :
        return

    # con = {}
    # for i in range(len(points)): # 点由字符表示转为由数字表示
    #     con[i] = points[i]
    # print(con)

    S = []
    T = []
    # 初始化
    S.append((0,-1,0))
    for i in range(1,len(points)):
        T.append([i,0 if edges[0][i]!=sys.maxsize else -1,edges[0][i]])
    print("初始化（默认第一个点作为源点）",S,T)



    while len(T)>0:
        tmp_min = T[0][2]
        min_point = 0
        for i in range(len(T)):
            if T[i][2]<tmp_min:
                tmp_min = T[i][2]
                min_point = i
        print("从T中取出第",min_point+1,"个")
        S.append(T[min_point])
        T.pop(min_point)


        for i in T: # 更新
            if edges[S[-1][0]][i[0]] !=sys.maxsize:
                if edges[S[-1][0]][i[0]] + S[-1][-1] < i[2]:
                    i[1] = S[-1][0]
                    i[2] = edges[S[-1][0]][i[0]] + S[-1][-1]
        print("迭代",S,T)


    print(S)
    return S



if __name__ == '__main__':
    # 有向图,示例参考https://blog.csdn.net/luoshixian099/article/details/51918844
    edges = [[sys.maxsize for i in range(6)] for  j in range(6)]
    edges[0][1] = 50
    edges[0][2] = 10
    edges[0][4] = 45
    edges[1][2] = 15
    edges[1][4] = 10
    edges[2][0] = 20
    edges[2][3] = 15
    edges[3][1] = 20
    edges[3][4] = 35
    edges[3][5] = 3
    edges[4][3] = 30
    print("邻接表(有向):",edges)
    points = ['a','b','c','d','e','f']
    r = Dijkstra(edges,points)