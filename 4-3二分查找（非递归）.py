def binsearch(num,target):
    left = 0
    right = len(num)-1

    while left<=right:
        mid = (left + right) // 2
        if num[mid]==target:
            return mid
        elif num[mid]<target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

r = binsearch([3],21)
print(r)
