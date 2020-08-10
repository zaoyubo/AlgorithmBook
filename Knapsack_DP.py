import pprint
def Knapsack(w,v,c,n):
    '''

    :param w: 背包物品重量list
    :param v: 背包物品价值list
    :param c: 背包容量
    :param n: 背包可选物品个数 ，即len(w)
    :return: 最大价值
    '''
    dp = [ [0 for i in range(c+1)] for i in range(n+1) ] # 第0行空闲
    w.insert(0,-1) # 添加空闲
    v.insert(0,-1) # 添加空闲

    # 第一行单独处理
    for j in range(c+1):
        if j >= w[1]:
            dp[1][j] = v[1]
    # print(dp)

    # 其他行
    for i in range(2,n+1):
        for j in range(c+1):
            if j-w[i]>=0:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-w[i]]+v[i])
            else:
                dp[i][j] = dp[i-1][j]

    pprint.pprint(dp)
    return dp[n][c]










if __name__ == '__main__':
    # w,c 必须为整数
    w = [2, 2, 6, 5, 4]
    v = [6, 3, 5, 4, 6]
    c = 10
    r = Knapsack(w,v,c,len(w))
    print(r)
