def nqueen(a,loc,vis):
    if(loc==len(a)):
        print(a)
        return
    for i in range(0,n):
        if(vis[i]==0 and checkdiag(a,loc,i)):
            vis[i]=1
            a[loc][i]=1
            nqueen(a,loc+1,vis)
            a[loc][i]=0
            vis[i]=0

def checkdiag(a,row,col):
    i,j=row,col
    while(i>-1 and j>-1):
        if(a[i][j]==1):
            return False
        i-=1
        j-=1
    i,j=row,col
    while(i>-1 and j<len(a)):
        if(a[i][j]==1):
            return False
        i-=1
        j+=1
    return True
print("Enter no of queens : ")
n=int(input())
l=[]
for i in range(0,n):
    b=[0]*n
    l.append(b)
vi=[0]*n
nqueen(l,0,vi)
