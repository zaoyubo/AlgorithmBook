def Sort(num):#升序
    MergeSort(num,0,len(num)-1)
def Merge(num,left,mid,right):
    tmp = []
    i = left
    j = mid+1
    while i<=mid and j<=right:
        if num[i]>num[j]:
            tmp.append(num[j])
            j+=1
        else:
            tmp.append(num[i])
            i+=1
    while i<=mid:
        tmp.append(num[i])
        i += 1
    while  j<=right:
        tmp.append(num[j])
        j+=1
    for i in range(left,right+1):
        num[i]= tmp[i-left]
def MergeSort(num,left,right): # 将num数组中，left到right这一段归并排序，结果储存在num中
    if left<right:
        mid = (left+right)//2
        MergeSort(num,left,mid)
        MergeSort(num,mid+1,right)
        Merge(num,left,mid,right)










num = [8,4,5,7,1,3,6,2]
Sort(num)
print(num)