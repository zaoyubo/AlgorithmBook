



def LCSLength(X,Y):
    # c[i][j]代表序列Xi和Yj的最长公共子序列的长度
    c = [[0 for i in range(1+len(X))] for j in range(1+len(Y))]
    # b[i][j]:回溯时的方向 1--左上 2--向上 3--向左
    b =  [[0 for i in range(1+len(X))] for j in range(1+len(Y))]
    for i in range(len(X)+1):

        for j in range(len(Y)+1):

            if i==0 or j ==0:
                continue
            elif X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = 1
            else:
                if c[i-1][j]>=c[i][j-1]: # 注意“=”
                    c[i][j] = c[i-1][j]
                    b[i][j] = 2
                else:
                    c[i][j] = c[i][j-1]
                    b[i][j] = 3


    # 回溯得到子序列（答案不唯一）
    i = len(X)
    j = len(Y)
    l = []
    while i>0 and j>0:
        if b[i][j] == 1:
            l.insert(0,A[i-1])
            i -= 1
            j -= 1
        elif b[i][j] == 2:
            i-=1
        else:
            j-=1
    return l





if __name__ == '__main__':
    A = ['A','B','C','B','D']
    B = ['B','D','C','A','B']
    result = LCSLength(A,B)
    print("最长公共子序列长度是",len(result),"序列是",result,"（序列不唯一）")