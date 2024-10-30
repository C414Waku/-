class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.pre=None

class DoubleNodeList:
    def __init__(self):
        self.head=None
        
    def insertHead(self,x):
        nodex=Node(x)
        self.head=nodex
        self.head.next=self.head
        self.head.pre=self.head
    
    def insert(self,y,x):
        nodex=Node(x)
        tmp=self.head
        count=0
        while True:
            if tmp==self.head and count:
                print("雙向鏈結串列中沒有 ",y)
                break
            if tmp.data==y:
                nodex.next=tmp.next
                tmp.next=nodex
                nodex.pre=tmp
                nodex.next.pre=nodex
                break
            count+=1
            tmp=tmp.next
    def remove(self,x):
        tmp=self.head
        count=0
        while True:
            if tmp==self.head and count:
                print("雙向鏈結串列中沒有 ",x)
            if tmp.data==x:
                if x==self.head.data:
                    if tmp.next==self.head:
                        self.head=None
                    else:
                        tmp.pre.next=tmp.next
                        tmp.next.pre=tmp.pre
                        self.head=tmp.next
                    break
                tmp.pre.next=tmp.next
                tmp.next.pre=tmp.pre
                break
            tmp=tmp.next
            count+=1
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
        while True:
            if count!=0 and tmp==self.head:
                break
            count+=1
            tmp=tmp.next
        print("雙向鏈結串列長度為 ",count)            

def test():
    li=DoubleNodeList()
    li.insertHead(4)
    li.insert(4,2)
    li.insert(4,3)
    li.insert(4,6)
    li.insert(6,8)
    li.insert(8,9)
    li.printList()
    li.printLen()
    li.remove(4)
    li.printList()
    li.printLen()


test()