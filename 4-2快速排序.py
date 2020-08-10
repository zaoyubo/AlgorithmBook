def put_pivot(num,left,right):
    pivot = num[left]
    i = left
    j = right
    while i<j:
        while  num[j]>=pivot and i<j:
            j-=1
        num[i]=num[j]
        while  num[i]<=pivot and i<j:
            i+=1
        num[j]=num[i]
    num[i] = pivot
    return i

def divide_conquer(num,left,right):# 对left和right之间的段落进行排序，结果仍存放在num中
    if left<right: # 边界限制
        i = put_pivot(num,left,right)
        divide_conquer(num,left,i-1)
        divide_conquer(num,i+1,right)
def QuickSort(num):
    divide_conquer(num,0,len(num)-1)


num = [49,38,65,97,76,13,27,49]
QuickSort(num)
print(num)