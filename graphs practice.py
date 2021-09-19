n=int(input("Enter number of nodes:"))
e=int(input("Enter number of edges:"))
stack=[[] for j in range(n+1)]
for i in range(e):
    u=int(input())
    v=int(input())
    stack[u].append(v)
    stack[v].append(u)
print(stack)
