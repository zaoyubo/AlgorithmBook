def sort_by_ratio(item):
    return item[1]
def Knapsack(w,v,c):
    ratio = []
    r = [0 for i in range(len(w))]
    for i in range(len(w)):
        ratio.append((i,v[i]/w[i]))  # 比重越大，越值得放入背包
    ratio.sort(key=sort_by_ratio,reverse=True)
    print("根据价值与重量比值降序排列",ratio)
    tmp_c = c
    total = 0
    for i in range(len(w)):
        if w[ratio[i][0]]<tmp_c:
            r[ratio[i][0]]  =1
            tmp_c = tmp_c - w[ratio[i][0]]
            total += v[ratio[i][0]]
        elif tmp_c > 0:
            r[ratio[i][0]] = tmp_c/w[ratio[i][0]]
            total += v[ratio[i][0]] * r[ratio[i][0]]
            break
    print("解向量",r)
    print("最大总价值",total)

if __name__ == '__main__':
    w = [20,30,10]
    v = [60,120,50]
    r = Knapsack(w,v,50)

