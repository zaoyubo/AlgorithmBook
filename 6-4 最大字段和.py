def MaxSum(num):
    left = 0
    right = len(num)-1
    b = [0 for i in range(len(num))] # 以num[j]为结尾的最大字段和

    if num[0]<=0:
        b[0] = 0
        left = 1
    max_sum = 0
    for i in range(1,len(num)):
        b[i] = max(0,num[i]+b[i-1])
        if b[i]==0:
            left = i+1
        if b[i]>max_sum:
            max_sum = b[i]
            right =i
    return max_sum,num[left:right+1].copy()






if __name__ == '__main__':
    num = [-2, 11, -4, 13, -5, -2]
    r = MaxSum(num)
    print(r)