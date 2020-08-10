num = [1,2,3,4,5]

def BubbleSort(num): #升序
    count = 0
    for j in range(len(num)-1,0,-1):
        isSwap = 0 # 改进，如果某次没有交换，即已完成排序，便停止
        for i in range(j):
            count += 1
            if num[i]> num[i+1]:
                isSwap = 1
                t = num[i]
                num[i] = num[i+1]
                num[i+1] = t
        if isSwap==0:
            break
    print(count)
BubbleSort(num)
print(num)
