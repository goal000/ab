def dls(a,vis,src,c,dlmt):
    for i in range(0,len(a)):
        if(a[src][i]==1 and  vis[i]==0 and c<dlmt):
            print(i,end=" ")
            vis[i]=1
            dls(a, vis, i, c + 1, dlmt)
print("Enter no of vertices : ")
n=int(input())
a=[]
for i in range(0,n):
    b=[0]*n
    a.append(b)
print("Enter no of edgs  : ")
edgs=int(input())
print("Enter edgs from src to dest : ")
for i in range(0,edgs):
    src,des=map(int,input().split(" "))
    a[src][des]=1
    a[des][src]=1
vis=[0]*n
print("Enter limit to search : ")
dlmt=int(input())
print(0,end=" ")
vis[0]=1
dls(a,vis,0,0,dlmt)
