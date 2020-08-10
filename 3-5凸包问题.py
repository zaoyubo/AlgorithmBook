x=[1,6,5,5]
y = [1,1,5,3]
# 判断x3,y3在其他连个点的什么位置
def where (x1,y1,x2,y2,x3,y3):
     # print(x1,y1,x2,y2,x3,y3)
     a = y2-y1
     b = x1-x2
     c = -x2*y1 + x1*y2
     if a*x3+b*y3 > c:
         # print(-1)
         return -1 # 下侧

     elif a*x3+b*y3 < c:
         # print(1)
         return 1 # 上侧
     else:
         # print(0)
         return 0 # 点在线上
def ConvexHull(x,y):
    pole = []
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            up = False
            down = False
            on = False
            for k in range(len(x)):
                if k==i or k==j :
                    continue
                if where(x[i],y[i],x[j],y[j],x[k],y[k])==1:
                    up = True
                elif where(x[i],y[i],x[j],y[j],x[k],y[k])==-1:
                    down = True
                else :
                    if x[k]<min(x[i],x[j]) or x[k]>max(x[i],x[j]) or y[k]<min(y[i],y[j]) or y[k]>max(y[i],y[j]):
                        break
                    else:
                        on = True
                if up and down:
                    break
            if (not (up and down))  :
                if (x[i],y[i]) not in pole:
                    pole.append((x[i],y[i]))
                if (x[j], y[j]) not in pole:
                    pole.append((x[j], y[j]))
    return pole


print(ConvexHull(x,y))



