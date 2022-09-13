G = []

def Init(path,G):
    f = open(path)
    n = int(f.readline(), base = 10)
    for i in range(n+1):
        G.append([])
        for j in range(n+1):
            G[i].append(0)
    while True:
        string = f.readline();
        if not string:
            break
        string = string.replace('\t',' ')
        k =string.index(' ')
        str = string[0:k]
        i = int(str,base=10)
        m = string.index(' ',k+1,-1)
        str = string[k+1:m]
        j = int(str,base = 10)
        str = string[m+1:len(string)]
        x = int(str,base = 10)
        G[i][j] = G[j][i] = x
    f.close()
    return n

def ViewMaTrix(G,n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print("%d" % G[i][j],end = ' ')
        print()

def DFS(u,n):
    S = []
    C = []
    for j in range(n+1):
        S.append(0)
        C.append(0)
    top = 1
    S[top] = u
    while top > 0:
        u = S[top]
        top -=1
        if C[u] ==1:
            continue
        print("%d" % u, end = '\t')
        C[u] = 1
        for i in range(1,n+1):
            v = n+1 -i
            if G[u][v] != 0 and C[v] == 0:
                top+=1
                S[top] = v
def main():
    n = Init("E:\Python\graph.inp",G)
    print("Xem ma tran G: ",end = "\n")
    #ViewMaTrix(G,n)
    u = 1
    DFS8 (u,n)
if __name__ == "__main__":
    main()


            



