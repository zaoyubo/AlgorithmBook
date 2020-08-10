def binsearch(num,left,right,target):
    if left>right: # 边界限制
        return
    mid = (left+right)//2
    if num[mid] == target:
        return mid
    if num[mid]>target:
        r = binsearch(num,left,mid-1,target)
    else:
        r = binsearch(num,mid+1,right,target)

    return r if r else -1 # 可能找不到
r = binsearch([5],0,0,21)
print(r)