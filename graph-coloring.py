def issafe(a,vert,c,n,colour):
    for i in range(0,n):
        if(a[vert][i]==1 and colour[i]==c):
            return False
    return True
def colouring(ncol,n,color,a):
        if colorutil(ncol,n,color,a,0)==None:
            print("Can't colour given grapgh ")
        else:
            print("Assign colrs : ")
            for i in range(0,len(color)):
                print(color[i],end=" ")
def colorutil(ncol,n,color,a,loc):
    if loc==n:
        return True
    for i in range(1,ncol+1):
        if(issafe(a,loc,i,n,color)==True):
            color[loc]=i
            if colorutil(ncol,n,color,a,loc+1)==True:
                return True
            color[loc]=0

print("Enter no of vertices : ")
n=int(input())
a=[]
for i in range(0,n):
    b=[0]*n
    a.append(b)
print("Enter no edges : ")
edgs=int(input())
print("Enter edges from src to dest ")
for i in range(0,edgs):
    l1,l2=map(int,input().split(' '))
    a[l1][l2]=1
    a[l2][l1]=1
print("Enter no of colors : ")
ncol=int(input())
color=[0]*n
colouring(ncol,n,color,a)