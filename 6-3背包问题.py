def Knapsack(w,v,c):
    m = [ [0 for i in range(c+1)] for j in range(len(w)) ]
    for i in range(len(w)-1,0,-1):
        for j in range(c+1):
            if i==len(w)-1 and j >= w[i]:
                m[i][j] = v[i]
            elif i<len(w)-1:
                if j<w[i]:
                    m[i][j] = m[i+1][j]
                else:
                    m[i][j] = max(m[i+1][j],m[i+1][j-w[i]]+v[i])
    m[0][c] = max(m[1][c],m[1][c-w[0]]+v[0]) # 第一行只需要计算一个
    print(m)
    return m

def Traceback(m,w):
    if len(m)==0:
        return

    x = [0 for i in range(len(v))]
    tmp = len(m[0])-1
    for i in range(len(v)):
        if i == len(v)-1:
            if m[i][tmp] == 0:
                x[i]=0
            else:
                x[i]=1
            break
        if m[i][tmp] == m[i+1][tmp]:
            x[i]=0
        else:
            x[i]=1
        tmp = tmp - w[i]
    print(x)
    return x


if __name__ == '__main__':
    w = [2,2,6,5,4]
    v = [6,3,5,4,6]
    c = 10
    m = Knapsack(w,v,c)
    t = Traceback(m,w)
    print('最优解为:',t,"物品总价值最大为",m[0][c])