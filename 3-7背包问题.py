# 子集问题



def Knapsack(w,v,W):
    bit = [0]*len(w)
    max_value = 0
    target = []

    for i in range(2**len(w)):
        weight = 0
        value = 0
        for j in range(len(w)):
            if bit[j]==1:
                weight += w[j]
        if weight<=W:
            for j in range(len(v)):
                if bit[j] == 1:
                    value += v[j]
            if value>max_value:
                max_value = value
                target = bit.copy()
        if bit[len(bit) - 1] == 0:
            bit[len(bit) - 1] = 1
        else:
            for k in range(len(bit)-1,-1,-1):
                if bit[k]==1:
                    bit[k] =0
                else:
                    bit[k]=1
                    break
    return (max_value,target)

r = Knapsack([2,2,6,5],[6,3,5,4],10)
print(r)

