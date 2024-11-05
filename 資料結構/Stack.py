class Stack():
    def __init__(self,x) :
        self.size=x
        self.data=[0]*self.size
        self.top=-1

    def isFull(self):
        return self.top==self.size-1
    
    def isEmpty(self):
        return self.top==-1
    
    def push(self,x):
        if self.isFull():
            print("堆疊已滿")
        else:
            self.top+=1
            self.data[self.top]=x
    
    def pop(self):
        if self.isEmpty():
            print("堆疊已空")
        else:
            data=self.data[self.top]
            self.top-=1
            return data     

    def printStack(self):
        if not self.isEmpty():
            for i in range(0,self.top+1):
                print(self.data[i],end=" ")
            print()

def test():
    s=Stack(4)
    for i in range(1,5):
        s.push(i)
        s.printStack()
    for i in range(1,5):
        s.pop()
        s.printStack()

test()