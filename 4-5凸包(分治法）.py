import sys
import matplotlib.pyplot as plt

class ConvexHull:
    # points:[(1,2),(3,4),...]
    def __init__(self,points):
        plt.figure(figsize=(8, 5))
        plt.ion()
        plt.grid(True)

        self.points = points

        # 绘制点
        plt.cla()
        x = []
        y = []
        for i in points:
            x.append(i[0])
            y.append(i[1])
        plt.scatter(x, y)
        plt.pause(0.2)




    def sort_by_x(self,elem):
        return elem[0]

    # 点p3到直线(p1,p2)的距离，行列式
    def dis(self,p1,p2,p3):
        return p1[0]*p2[1] + p3[0]*p1[1] + p2[0]*p3[1] - p3[0]*p2[1] -p2[0]*p1[1] -p1[0]*p3[1]

    # 找出半部分的极点
    def UpperOrLower(self,points,flag,max_point,left_point,right_point):
        plt.plot([left_point[0], max_point[0]], [left_point[1], max_point[1]], color="red")
        plt.plot([max_point[0], right_point[0]], [max_point[1], right_point[1]], color="red")
        plt.pause(1)
        if len(points)<=3:
            x = []
            y = []
            for i in points:
                x.append(i[0])
                y.append(i[1])
            plt.scatter(x, y, color="black", s=200)
            plt.pause(1)
            return points


        max_distance = 0
        points_l  =[]
        max_point_l =left_point
        for i in range(0,len(points)):
            distance = self.dis(left_point,max_point,points[i])
            if distance*flag > 0:
                points_l.append(points[i])
                if distance*flag>max_distance:
                    max_distance = distance
                    max_point_l = points[i]
        max_distance_r = 0
        points_r = []
        max_point_r = right_point
        for j in range(0,len(points)):
            distance = self.dis(max_point, right_point, points[j])
            if distance *flag > 0:
                points_r.append(points[j])
                if distance *flag> max_distance_r:
                    max_distance_r = distance
                    max_point_r = points[j]

        points_l.append(left_point)
        points_l.append(max_point)
        points_r.append(right_point)
        points_r.append(max_point)

        rl = self.UpperOrLower(points_l,1,max_point_l,left_point,max_point)
        ru = self.UpperOrLower(points_r, -1, max_point_r, max_point,right_point )


        return list(set(rl+ru))

    def Convex_Hull(self):
        points = self.points

        if len(points)<=3:
            return points

        points.sort(key=self.sort_by_x)
        left_point = points[0]
        right_point = points[-1]

        upper = []
        lower = []
        upper_max = 0
        lower_max = 0

        for i in range(len(points)):
            distance = self.dis(left_point,right_point,points[i])
            if distance == 0:
                upper.append(points[i])
                lower.append(points[i])
            elif distance > 0:
                upper.append(points[i])
                if distance > upper_max:
                    upper_max = distance
                    upper_point = points[i]
            else:
                lower.append(points[i])
                if distance < lower_max:
                    lower_max = distance
                    lower_point = points[i]

        ru = self.UpperOrLower(upper,1,upper_point,left_point,right_point)
        rl = self.UpperOrLower(lower,-1,lower_point,left_point,right_point)

        result = list(set(ru+rl))

        # x=[]
        # y=[]
        # for i in result:
        #     x.append(i[0])
        #     y.append(i[1])
        # plt.scatter(x,y,color="black",s=200)
        # plt.pause(1)

        plt.ioff()
        plt.show()
        return result










points = [(0,0),(1,-1),(4,-3),(5,-3),(8,0),(3,-1),(5,-2),(2,1),(5,3),(4,4),(6,3)]
# points = [(0,0),(1,-1),(1,1),(2,0)]
# points = [(0,0),(4,4),(6,3),(8,0),(4,-4),(6,-3)]


test = ConvexHull(points)
result = test.Convex_Hull()
print(result)
