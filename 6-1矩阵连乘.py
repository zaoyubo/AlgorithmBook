#   A0     A1     A2      A3      A4      A5
#   30*35  35*15  15*5    5*10    10*20   20*25
#p: 30  35 15  5 10 20 25 代表A0-A5矩阵连乘

def MatrixChain(p):
# 二维列表m:m[i][j]存储从A[i]到A[j]的连乘（包括A[i]和A[j])的最少数乘次数
#    0 1 2 3 4 5
#0   x x x x x x  \ \ \ \ \ \
#1   - x x x x x   \ \ \ \ \
#2   - - x x x x    \ \ \ \
#3   - - - x x x     \ \ \
#4   - - - - x x      \ \
#5   - - - - - x       \
# 二维列表s:m[i][j]记录的最少数乘次数对应的第一次分割,如：3,将A[i][j]分为A[i][3]和A[i+1][j]

    m = [[0 for i in range(len(p)-1)] for j in range(len(p)-1)]
    s = [[-1 for i in range(len(p)-1)] for j in range(len(p)-1)]
    for j in range(1,len(p)-1):
        for i in range(len(p)-1):
            if i+j == len(p)-1:
                break
            l=[]
            for k in range(i,i+j):
                time = m[i][k] + m[k+1][i+j] +p[i]*p[k+1]*p[i+j+1]
                l.append(time)
            m[i][i+j] = min(l)
            s[i][i+j] = l.index(min(l)) + i

    return m,s

def path(s,l,r):
    if l+1 == r:
        return(l,r)
    if l==r:
        return l

    mid = s[l][r]
    rl = path(s,l,mid)
    rr = path(s,mid+1,r)
    return (rl,rr)


def Traceback(s,i,j): # 其他回溯路径的方式
    if i==j:
        return
    Traceback(s,i,s[i][j])
    Traceback(s,s[i][j]+1,j)
    print("Multiply A",i,s[i][j]," and A",(s[i][j]+1),j)


p=[30,35,15,5,10,20,25]
result = MatrixChain(p)
print("最小数乘次数:",result[0][0][len(p)-2])
result_path = path(result[1],0,len(p)-2)
print(result_path)
Traceback(result[1],0,len(p)-2)
