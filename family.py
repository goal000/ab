class Main:
    def __init__(self,s):
        self.a=[]
        self.a.append(s)
    def birth(self,par,child):
        if par in self.a:
            self.a.append(child)
        else:
           self.a.append(par)
           self.a.append(child)
    def death(self,person):
        self.loc=-1
        for i in range(0,len(self.a)):
            if(self.a[i]==person):
                self.loc=i
                break
        if(self.loc!=-1):
            while(self.loc<len(self.a)-1):
                self.a[self.loc]=self.a[self.loc+1]
                self.loc=self.loc+1
            self.a.pop()
    def inhert(self):
        print(self.a)
ob=Main('paul')
ob.birth('Paul', 'Zach')
ob.birth('Paul', 'Jesse')
ob.birth('Jesse', 'Ursula')
ob.birth('Jesse', 'Ryan')
ob.birth('Jesse', 'Thea')
ob.death('Paul')
ob.inhert()
ob.death('Zach')
ob.inhert()       
    
        