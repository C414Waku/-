class Node():
    
    def __init__(self,x):
        self.data=x
        self.next=None

class CircleNodeList():
    
    def __init__(self) :
        self.head=None
    
    def insertHead(self,x):
        self.head=Node(x)
        self.head.next=self.head
    
    def insert(self,y,x):
        nodex=Node(x)
        tmp=self.head
        flag=False        
        while True:
            if flag and tmp==self.head:
                print("串列中沒有",y)
                break
            flag=True
            if tmp.data==y:
                nodex.next=tmp.next
                tmp.next=nodex
                break
            tmp=tmp.next

    def remove (self,x):
        tmp=self.head.next
        before=self.head
        flag=False
        while True:
            if flag and before==self.head:
                print("串列中沒有",x)
                break
            flag=True
            if tmp.data==x:
                if x==self.head.data:
                    if self.head.next==self.head:
                        self.head=None
                        self.head.next=None
                    else:
                        self.head=self.head.next
                        before.next=self.head                        
                else:
                    before.next=tmp.next
                break
            before=tmp
            tmp=tmp.next

    def printList(self):
        tmp=self.head
        flag=False
        while True:
            if flag and tmp==self.head:
                break
            flag=True
            print(tmp.data,end=" ")
            tmp=tmp.next
        print()

    def printLen(self):
        tmp=self.head
        count=0
        flag=False
        while True:
            if flag and tmp==self.head:
                break
            flag=True
            count+=1
            tmp=tmp.next
        print("串列長度為",count)

def test():
    li=CircleNodeList()
    li.insertHead(5)
    li.insert(5,2)
    li.insert(5,4)
    li.insert(3,8)
    li.printList()
    li.remove(5)
    li.remove(9)
    li.printList()
    li.insert(4,9)
    li.printList()
    li.remove(8)
    li.printList()
    li.printLen()

test()