import math
import sys
def dis(a,b):
    x = abs(a[0]-b[0])
    y = abs(a[1]-b[1])
    return math.sqrt(x**2+y**2)
def sort_y(elem):
    return elem[1]
def sort_x(elem):
    return elem[0]
# points：按x坐标排好序的点[(1,2),(3,2),...]
# 查找points中left-right部分的最近点对，返回距离
def cloest_pair(points,left,right):
    if (right-left+1)<=3:
        min_dis = sys.maxsize
        for i in range(left,right+1):
            for j in range(i+1,right+1):
                min_dis = min(dis(points[i],points[j]),min_dis)
        return min_dis

    mid = (right-left)//2
    dl = cloest_pair(points,left,mid)
    dr = cloest_pair(points,mid+1,right)
    d = min(dl,dr)

    i = mid
    j = mid
    while points[mid][0] - points[i][0] < d:
        i-=1
    while points[j][0] - points[mid][0] <= d:
        j+=1
    tmp = points[i+1:j].copy()
    tmp.sort(key=sort_y)
    for i in range(len(tmp)):
        for j in range(i+1,len(tmp)):
            if points[j][1]-points[i][1]>d:
                break
            d = min(d,dis(points[i],points[j])<d)
    return d

points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
points.sort(key=sort_x)
result = cloest_pair(points,0,5)
print(result)