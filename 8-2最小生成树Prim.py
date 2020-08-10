# -*- coding:utf-8 -*-
import sys

def sort_by_minedge(item):
    return item[2]

def Prim(edges,points):

    if not points or len(points)<=0 :
        return



    con = {}
    for i in range(len(points)): # 点由字符表示转为由数字表示
        con[i] = points[i]
    # print(con)

    U = []
    V = [] # 表示算法书中U-V
    target_edge = []
    # 初始化
    U.append(0)
    for i in range(1,len(points)):
        V.append([i,0 if edges[i][0]!=-1 else -1,edges[i][0]])
    print("初始化（选择第一个点作为起始点）",U,V)



    while len(V)>0:
        V.sort(key=sort_by_minedge) # 由于目的仅仅是找到最小的，其实不需要排序，循环一次便可以找到
        i = 0
        while V[i][2]==-1:
            i+=1
        U.append(V[i][0])

        target_edge.append((V[i][0],V[i][1]))
        V.pop(i)

        for i in V: # 由于U中只新增了一个点，因此对V中每个点比较更新一次即可
            if edges[i[0]][U[-1]] >0:
                if i[2]==-1 or edges[i[0]][U[-1]] < i[2]:
                    i[1] = U[-1]
                    i[2] = edges[i[0]][U[-1]]


    print(target_edge)
    return target_edge



if __name__ == '__main__':
    edges = [[-1,7,-1,-1,9,4],[7,-1,2,-1,-1,-1],[-1,2,0,8,-1,6],[-1,-1,8,0,3,5],[9,-1,-1,3,0,5],[4,-1,6,5,5,0]]
    points = ['a','b','c','d','e','f']
    r = Prim(edges,points)