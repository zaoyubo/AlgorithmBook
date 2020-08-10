def sort_by_minedge(item):
    return item[2]
def findroot(k,parent):
    while parent[k]!= k:
        k = parent[k]
    return k
def Kruskal(edges_matrix,points):
    edges = []
    parent = [i for i in range(len(points))]
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            if edges_matrix[i][j]!= -1:
                edges.append((i,j,edges_matrix[i][j]))
    edges.sort(key=sort_by_minedge)
    print(edges)

    for i in edges:
        root1 = findroot(i[0],parent)
        root2 = findroot(i[1],parent)
        if root1==root2:
            continue
        else:
            parent[root1] = root2
            print(i)

    pass

if __name__ == '__main__':
    edges = [[-1,7,-1,-1,9,4],[7,-1,2,-1,-1,-1],[-1,2,0,8,-1,6],[-1,-1,8,0,3,5],[9,-1,-1,3,0,5],[4,-1,6,5,5,0]]
    points = ['a','b','c','d','e','f']
    r = Kruskal(edges,points)