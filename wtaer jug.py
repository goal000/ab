from collections import defaultdict
vis=defaultdict(lambda:False)
def water(l1,l2):
    if((l1==d and l2==0) or (l1==0 and l2==d)):
        print(l1,l2)
        return True
    if(vis[(l1,l2)]==False):
        print(l1,l2)
        vis[(l1,l2)]=True
        return water(0,l2) or water(l1,0) or water(jug1,l2) or water(l1,jug2) or water(l1+min(l2,jug1-l1),l2-min(l2,jug1-l1)) or water(l1+min(l1,jug2-l2),l2-min(l1,jug2-l2))
    return False
jug1=int(input())
jug2=int(input())
d=int(input())
water(0,0)

