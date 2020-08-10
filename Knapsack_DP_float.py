import pprint
import copy
def Knapsack(w,v,c,n):
    '''

    :param w: 背包物品重量list
    :param v: 背包物品价值list
    :param c: 背包容量
    :param n: 背包可选物品个数 ，即len(w)
    :return: 最大价值
    '''
    dp = [ [] for i in range(n+1) ] # 第0行跳跃点{(0,0)}
    w.insert(0,-1) # 添加空闲
    v.insert(0,-1) # 添加空闲

    # 第 0 单独处理
    dp[0].append((0,0))

    for i in range(1,n+1):
        p = copy.deepcopy(dp[i-1])
        q = copy.deepcopy(dp[i-1])
        for k in range(len(q)):
            # print(q,q[k][0],w[i])
            a = q[k][0]+w[i]
            b = q[k][1]+v[i]
            q[k] = (a,b)
        r = p + q
        r.sort()

        # [[(0, 0)],
        #  [(0, 0), (2, 6)],
        #  [(0, 0), (2, 6), (4, 9)],
        #  [(0, 0), (2, 6), (4, 9), (8, 11), (10, 14)],
        #  [(0, 0), (2, 6), (4, 9), (7, 10), (8, 11), (9, 13), (10, 14)],
        #  [(0, 0), (2, 6), (4, 9), (6, 12), (8, 15)]]
        # 15
        k = 1
        while k < len(r):
            if r[k][1] < r[k-1][1] and r[k][0] > r[k-1][0]: # 非跳跃点
                r.pop(k)
                k -= 1
            elif r[k][0] == r[k-1][0]: # 排在前面的是非跳跃点，删除
                r.pop(k-1)
                k -= 1
            elif r[k][0]>c: # 超出背包容量
                r.pop(k)
                k -= 1
            k += 1

        # print(p, q, r)
        dp[i] = r


    pprint.pprint(dp)
    return dp[-1][-1][1]










if __name__ == '__main__':
    # w,c 可以为 小数
    w = [2, 2, 6, 5, 4]
    v = [6, 3, 5, 4, 6]
    c = 10
    r = Knapsack(w,v,c,len(w))
    print(r)
