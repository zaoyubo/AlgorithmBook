x=[1,6,3]
y = [1,1,1]

# 假设不存在三点共线
def ConvexHull(x,y):
    pole = []
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            sign1 = 0 # 一侧的点数（包含在线上的点）
            sign2 = 0 # 另一侧的点数（包含在线上的点）
            a = y[j] - y[i]
            b = x[i] - x[j]
            c = x[i]*y[j] - x[j]*y[i]
            for k in range(len(x)):
                if k ==i or k==j :
                    continue
                if a*x[k] + b*y[k] > c:
                    sign1+=1
                elif a*x[k] + b*y[k] < c:
                    sign2+=1
                else:
                    sign1 += 1
                    sign2 += 1
            if sign2==len(x)-2 or sign1==len(x)-2:
                if (x[i],y[i]) not in pole:
                    pole.append((x[i],y[i]))
                if (x[j], y[j]) not in pole:
                    pole.append((x[j], y[j]))
    return pole

print(ConvexHull(x, y))