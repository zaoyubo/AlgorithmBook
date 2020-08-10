def MaxSum(num):
    left = 0
    right = len(num)-1
    b = [0 for i in range(len(num))] # 以num[j]为结尾的最大字段和

    if num[0]<=0:
        b[0] = 0
        left = 1
    else:
        b[0] = num[0]
    max_sum = 0
    for i in range(1,len(num)):
        b[i] = max(0,num[i]+b[i-1])
        if b[i]==0:
            left = i+1
        if b[i]>max_sum:
            max_sum = b[i]
            right =i
    return max_sum,left,right
def MaxMatrixSum(num):
    if len(num)<=0 or len(num[0])<=0:
        return
    m = len(num) # 行数
    n = len(num[0])
    max_sum_matrix = 0

    for i1 in range(m):
        row = [0 for i in range(n)]
        for i2 in range(i1,m):
            for j in range(n):
                    row[j] = row[j] + num[i2][j]
            r = MaxSum(row)
            max_sum = r[0]
            if max_sum > max_sum_matrix:
                max_sum_matrix = max_sum
                index = (i1,i2,r[1],r[2])
    return max_sum_matrix,index






if __name__ == '__main__':
    # 矩阵按行存储
    r = MaxMatrixSum([[0,-2,-7,0],[9,2,-6,2],[-4,1,-4,1],[-1,8,0,-2]])
    print("最大子矩阵和",r[0],"--- i1,i2,j1,j2:",r[1])

