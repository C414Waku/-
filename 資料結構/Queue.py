class Queue():
    def __init__(self,x):
        self.size=x
        self.data=[0]*self.size
        self.front=-1
        self.back=-1

    def isEmpty(self):
        return self.front==self.back
    
    def isFull(self):
        return self.back==self.size-1
    
    def enQueue(self,x):
        if self.isFull():
            print("佇列已滿")
        else:
            self.back+=1
            self.data[self.back]=x
    
    def deQueue(self):
        if self.isEmpty():
            print("佇列已空")
        else:
            self.front+=1
            return self.data[self.front]
    
    def printQueue(self):
        if not self.isEmpty:
            for i  in range(self.front+1,self.back+1):
                print(self.data[i],end=" ")
            print() 

def test():
    q=Queue(5)
    for i in range(6):
        q.enQueue(i+1)
        q.printQueue()
    for i in range(6):
        q.deQueue()
        q.printQueue()

test()
