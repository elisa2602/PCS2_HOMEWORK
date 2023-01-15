def tree(file):
    
    with open(file, "r") as f:
        n = int(f.readline().strip())
        arr = [[] for i in range(n)]
        visited = [False for i in range(n)]
        for adj in f:
            values = adj.split(" ")
            v1, v2 = int(values[0]), int(values[1])
            arr[v1-1].append(v2-1)
            arr[v2-1].append(v1-1)

    count = 0
    for i in range(len(visited)):
        if not visited[i]:
            visit(arr, visited, i)
            count+=1
    
    with open("resulttree.txt", "w") as f:
        f.write(str(count-1))
        
    return count-1
    
def visit(arr, visited, start):
    visited[start] = True
    for a in arr[start]:
        if not visited[a]:
            visit(arr, visited, a)

tree('rosalind_tree.txt')
    
            
        