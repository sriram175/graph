#bfs traversal for undirected graph
'''n=int(input())
e=int(input())
adj=[[] for i in range(n+1)]
for i in range(e):
    a=list(map(int,input().split()))
    u=a[0]
    v=a[1]
    adj[u].append(v)
    adj[v].append(u)
vis=[0]*(n+1)
res=[]
def bfs(i,vis,res):
    stack=[]
    stack.append(i)
    vis[i]=1
    while stack!=[]:
        node=stack.pop(0)
        res.append(node)
        for x in adj[node]:
            if vis[x]==0:
                vis[x]=1
                stack.append(x)
    return res
for i in range(1,n+1):
    res=[]
    if vis[i]==0:
        print(bfs(i,vis,res))'''
#dfs traversal for undirectd graph
'''n=int(input())
e=int(input())
adj=[[] for i in range(n+1)]
for i in range(e):
    a=list(map(int,input().split()))
    u=a[0]
    v=a[1]
    adj[u].append(v)
    adj[v].append(u)
res=[]
vis=[0]*(n+1)
def dfs(node,vis,res):
    res.append(node)
    vis[node]=1
    for k in adj[node]:
        if vis[k]==0:
            dfs(k,vis,res)
    return res
for i in range(1,n+1):
    res=[]
    if vis[i]==0:
        print(dfs(i,vis,res))'''
#cycle detection in undirected graph using bfs
'''n=int(input())
e=int(input())
adj=[[] for i in range(n+1)]
for i in range(e):
    a=list(map(int,input().split()))
    u=a[0]
    v=a[1]
    adj[u].append(v)
    adj[v].append(u)
print(adj)
vis=[0]*(n+1)
def bfs(node1,vis,par):
    vis[node1]=1
    stack=[]
    stack.append(node1)
    while stack!=[]:
        node=stack.pop(0)
        for k in adj[node]:
            if vis[k]==0:
                vis[k]=1
                par[k]+=node
                stack.append(k)
            elif vis[k]!=0 and par[node]!=k:
                return True
    return False
par=[0]*(n+1)
def fun():
    for i in range(1,n+1):
        if vis[i]==0:
            par[i]=-1
            if bfs(i,vis,par)==True:
                return True
    return False
if fun():
    print("cycle")
else:
    print("No cycle")'''
#cycle detection for undirected using dfs
'''n=int(input())
e=int(input())
adj=[[] for i in range(n+1)]
for i in range(e):
    a=list(map(int,input().split()))
    u=a[0]
    v=a[1]
    adj[u].append(v)
    adj[v].append(u)
vis=[0]*(n+1)
def dfs(node,vis,par):
    vis[node]=1
    for k in adj[node]:
        if vis[k]==0:
            if dfs(k,vis,node)==True:
                return True
        elif vis[k]!=0 and par!=k:
            return True
    return False
def fun():
    for i in range(1,n+1):
        if vis[i]==0:
            if dfs(i,vis,-1)==True:
                return True
    return False
if fun():
    print("Cycle")
else:
    print("No cycle")'''
#cycle detection for directed graph using dfs
'''n=int(input())
e=int(input())
adj=[[] for i in range(n+1)]
for i in range(e):
    a=list(map(int,input().split()))
    u=a[0]
    v=a[1]
    adj[u].append(v)
vis=[0]*(n+1)
dfsvis=[0]*(n+1)
def dfs(node,vis,dfsvis):
    for k in adj[node]:
        if vis[k]==0:
            vis[k]=1
            dfsvis[k]=1
            if dfs(k,vis,dfsvis)==True:
                return True
        elif vis[k]==1 and dfsvis[k]==1:
            return True
    return False
def fun():
    for i in range(1,n+1):
        if vis[i]==0:
            vis[i]==1
            dfsvis[i]==1
            if dfs(i,vis,dfsvis)==True:
                return True
    return True
if fun():
    print("Cycle")
else:
    print("No cycle")'''
#topological sort using dfs for acyclic directed graph
'''n=int(input())
e=int(input())
adj=[[] for i in range(n+1)]
for i in range(e):
    a=list(map(int,input().split()))
    u=a[0]
    v=a[1]
    adj[u].append(v)
vis=[0]*(n)
def dfs(node,vis,stack):
    vis[node]=1
    for k in adj[node]:
        if vis[k]==0:
            dfs(k,vis,stack)
    stack.append(node)
stack=[]
for i in range(n):
    if vis[i]==0:
        dfs(i,vis,stack)
print(stack[::-1])'''
#topological sort using bfs kahn's algorithm
'''n=int(input())
e=int(input())
count=[0]*(n)
adj=[[] for i in range(n+1)]
for i in range(e):
    a=list(map(int,input().split()))
    u=a[0]
    v=a[1]
    adj[u].append(v)
    count[v]+=1
queue=[]
def bfs(queue,adj,stack):
    while queue!=[]:
        node=queue.pop(0)
        stack.append(node)
        for k in adj[node]:
            count[k]-=1
            if count[k]==0:
                queue.append(k)
for i in range(n):
    if count[i]==0:
        queue.append(i)
stack=[]
bfs(queue,adj,stack)
print(stack)'''
#cycle detection using bfs kahn's algorithn
'''n=int(input())
e=int(input())
count=[0]*(n)
adj=[[] for i in range(n+1)]
for i in range(e):
    a=list(map(int,input().split()))
    u=a[0]
    v=a[1]
    adj[u].append(v)
    count[v]+=1
queue=[]
stack=[]
def bfs(queue,stack,adj):
    c=0
    while queue!=[]:
        node=queue.pop(0)
        stack.append(node)
        for k in adj[node]:
            count[k]-=1
            if count[k]==0:
                queue.append(k)
for i in range(n):
    if count[i]==0:
        queue.append(i)
bfs(queue,stack,adj)
if len(stack)==n:
    print("No cycle")
else:
    print("Cycle")'''
#bipartite graph using bfs
'''n=int(input())
e=int(input())
adj=[[] for i in range(n+1)]
for i in range(e):
    a=list(map(int,input().split()))
    u=a[0]
    v=a[1]
    adj[u].append(v)
    adj[v].append(u)
color=[0]*(n+1)
vis=[0]*(n+1)
def bfs(node1,vis,color):
    vis[node1]=1
    queue=[]
    queue.append(node1)
    while queue!=[]:
        node=queue.pop(0)
        for k in adj[node]:
            if vis[k]==0:
                vis[k]=1
                color[k]+=1-color[node]
                queue.append(k)
            elif vis[k]==1 and color[k]==color[node]:
                return False
    return True
def fun():
    for i in range(1,n+1):
        if vis[i]==0:
            color[i]==0
            if bfs(i,vis,color)==False:
                print(color)
                return False
    print(color)
    return True
if fun():
    print("Bi partite graph")
else:
    print("Not bi partite graph")'''
#bipartite graph using dfs
'''n=int(input())
e=int(input())
adj=[[] for i in range(n+1)]
for i in range(e):
    a=list(map(int,input().split()))
    u=a[0]
    v=a[1]
    adj[u].append(v)
    adj[v].append(u)
vis=[0]*(n+1)
color=[0]*(n+1)
def dfs(node,vis,color,adj):
    vis[node]=1
    for k in adj[node]:
        if vis[k]==0:
            color[k]=1-color[node]
            if dfs(k,vis,color,adj)==False:
                return False
        elif vis[k]==1 and color[k]==color[node]:
            return False
    return True
def fun():
    for i in range(1,n+1):
        if vis[i]==0:
            color[i]=1
            if dfs(i,vis,color,adj)==False:
                return False
    return True
if fun():
    print("Bipartite")
else:
    print("Not Bipartite")'''
#shortest path using bfs
'''n=int(input())
e=int(input())
adj=[[] for i in range(n)]
for i in range(e):
    a=list(map(int,input().split()))
    u=a[0]
    v=a[1]
    w=a[2]
    a=(v,w)
    b=(u,w)
    adj[u].append(a)
    adj[v].append(b)
dis=[10**6]*(n)
def bfs(node1,dis,adj):
    queue=[]
    queue.append(node1)
    while queue!=[]:
        node=queue.pop(0)
        for k in adj[node]:
            if dis[k[0]]>dis[node]+k[1]:
                queue.append(k[0])
                dis[k[0]]=dis[node]+k[1]
    return dis
for i in range(n):
    dis[i]=0
    print(bfs(i,dis,adj))
    break'''
#shortest path using dfs topological sort for directed graph
'''n=int(input())
e=int(input())
adj=[[] for i in range(n)]
for i in range(e):
    a=list(map(int,input().split()))
    u=a[0]
    v=a[1]
    w=a[2]
    a=(v,w)
    adj[u].append(a)
dis=[10**6]*(n+1)
res=[]
vis=[0]*(n+1)
def dfs(node,vis,res,adj):
    vis[node]=1
    for k in adj[node]:
        if vis[k[0]]==0:
            dfs(k[0],vis,res,adj)
    res.append(node)
for i in range(n):
    if vis[i]==0:
        dfs(i,vis,res,adj)
        res1=res[::-1]
dis[0]=0
print(res1)
def bfs(node1,dis,adj):
    queue=[]
    queue.append(node1)
    while queue!=[]:
        node=queue.pop(0)
        for k in adj[node]:
            if dis[k[0]]>dis[node]+k[1]:
                dis[k[0]]=dis[node]+k[1]
    return dis
for i in res1:
    if dis[i]!=10**6:
        print(bfs(i,dis,adj))'''
#shortest path for undirected using djikstras
'''from queue import PriorityQueue
n=int(input())
e=int(input())
adj=[[] for i in range(n+1)]
for i in range(e):
    a=list(map(int,input().split()))
    u=a[0]
    v=a[1]
    w=a[2]
    a=(v,w)
    b=(u,w)
    adj[u].append(a)
    adj[v].append(b)
priority=PriorityQueue()
a=(0,1)
dis=[10**6]*(n+1)
dis[1]=0
priority.put_nowait(a)
def bfs(i,priority,adj):
    while priority.qsize()!=0:
        node=priority.get_nowait()
        for k in adj[node[1]]:
            a=(k[1],k[0])
            if dis[k[0]]>dis[node[1]]+k[1]:
                dis[k[0]]=dis[node[1]]+k[1]
                priority.put_nowait(a)
for i in range(1,n+1):
    bfs(i,priority,adj)
    print(dis)
    break'''
#minimum spanning treee using prims algorithm
'''from queue import PriorityQueue
n=int(input())
e=int(input())
adj=[[] for i in range(n+1)]
for i in range(e):
    a=list(map(int,input().split()))
    u=a[0]
    v=a[1]
    w=a[2]
    a=(v,w)
    b=(u,w)
    adj[u].append(a)
    adj[v].append(b)
key=[10**6]*(n+1)
mst=[0]*(n+1)
key[1]=0
a=(0,1)
def bfs(i,mst,key,adj,prioriy):
    while priority.qsize()!=0:
        node=priority.get_nowait()
        for k in adj[node[1]]:
            if mst[k[0]]!=1:
                if key[k[0]]>k[1]:
                    key[k[0]]=k[1]
                    a=(k[1],k[0])
                    par[k[0]]=node[1]
                    priority.put_nowait(a)
        mst[k[0]]=1
priority=PriorityQueue()
priority.put_nowait(a)
par=[-1]*(n+1)
for i in range(1,n+1):
    bfs(i,mst,key,adj,priority)
    print(key[1:])
    print(par[1:])
    break'''
