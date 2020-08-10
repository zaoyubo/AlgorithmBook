class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.symbol = None
def AddToHeap(heap,item):
    heap.append(item)
    i = len(heap)-1
    parent = (i+1)//2-1
    while i > 0 and (heap[i].key < heap[parent].key):
        heap[i],heap[parent] = heap[parent],heap[i]
        i = parent
        parent = (i+1)//2-1

# 向下调整最小堆
def AjustHeap(heap,i): # 引用传递
    k = i
    while (k <= len(heap) // 2 - 1):
        min_index = k
        if 2 * k + 1 <= len(heap) - 1 and heap[2 * k + 1].key < heap[min_index].key:
            min_index = 2 * k + 1
        if 2 * k + 2 <= len(heap) - 1 and heap[2 * k + 2].key < heap[min_index].key:
            min_index = 2 * k + 2

        if min_index != k:
            heap[min_index], heap[k] = heap[k], heap[min_index]
            min_index, k = k, min_index
        else:
            break

# 取出最小值，并调整
def extract(heap):
    r = heap[0]
    heap[0],heap[-1] = heap[-1],heap[0]
    heap.pop(len(heap)-1)
    AjustHeap(heap,0)
    return r

def printcode(root,code):
    t = root
    if t.symbol!=None:
        print(code,'-->',t.symbol)
        return
    if t.left!=None:
        printcode(t.left,code+'0')
    if t.right!=None:
        printcode(t.right,code+'1')

def Huffman(symbol,frequency):
    heap = []
    for i in range(len(frequency)):
        n = Node(frequency[i])
        n.symbol = symbol[i]
        heap.append(n)
    # 构建最小堆
    for i in range(len(heap)//2-1,-1,-1):
        AjustHeap(heap,i)

    print("初始小根堆:",end="")
    for i in heap:
        print(i.key,end=",")
    print("\b")

    for cnt in range(len(symbol)-1):
        a = extract(heap)
        # print("取出第一个",a.key)
        # for i in heap:
        #     print(i.key, end=",")
        # print("\b")
        b = extract(heap)
        # print("取出第二个",b.key)

        # for i in heap:
            # print(i.key, end=",")
        # print("\b")

        c = Node(a.key+b.key)


        c.left = a
        c.right = b
        AddToHeap(heap,c)
        # for i in heap:
        #     print(i.key, end=",")
        # print("\b")

    # print(heap[0].right.right.right.key)

    printcode(heap[0],"")


if __name__ == '__main__':
    symbol = ['F','O','R','G','E','T']
    frequency = [2,3,4,4,5,7]
    r = Huffman(symbol,frequency)
    # print(r)