
'''
所有数组从0开始计数，会和之前有些出入
'''

def getMinMax(i,j,k,m,n,op):
    '''
    获得 minf m[i][j][k] 和 maxf m[i][j][k]
    :param i: 开始的点编号
    :param j: 链的长度
    :param k: 被分割后，前面的链的长度
    :param m: dp数组
    :param n: 原问题链的长度，因为可能从i数k个后index超出n，需要n取余
    :return: (minf m[i][j][k] , maxf m[i][j][k])
    '''
    a = m[i][k][0]
    b = m[i][k][1]

    r = (i+k+1) % n
    c = m[r][j-k-1][0]
    d = m[r][j-k-1][1]

    if op[r]=='+':
        return (a+c,b+d)
    else:
        return (min(b*c,b*d,a*c,a*d), max(b*c,b*d,a*c,a*d))


    pass

def polygame(n,op,v):
    '''
    计算多边形游戏得分
    :param n: 点的个数
    :param op: 运算符数组 从0计数
    :param v: 点数组
    :return: (highest score,[removed_edges])
    '''
    m = [[[-1 for i in range(2)] for i in range(n)] for i in range(n) ]

    for i in range(n):
        m[i][0][0] = m[i][0][1] = v[i]

    for j in range(1,n):
        for i in range(0,n):
            for k in range(0,j): # 链i——i+j-1最后合并的地方
                if k == 0:
                    m[i][j][0],m[i][j][1] =  getMinMax(i,j,k,m,n,op)
                else:
                    minf,maxf = getMinMax(i, j, k, m, n, op)
                    m[i][j][0],m[i][j][1] = min(minf,m[i][j][0]),max(maxf,m[i][j][1])
    print(m)

if __name__ == '__main__':
    op = ['+', '+', '*', '*']
    v = [-7, 4, 2, 5]
    polygame(len(op),op,v)
    # 4
    # t -7 t 4 x 2 x 5