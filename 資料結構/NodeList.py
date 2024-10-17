
class Node() :
    def __init__(self,x):
        self.data=x
        self.next=None

class NodeList():
    def __init__(self) :
        self.head=None

    #新增第一筆資料
    def insertHead (self,x):
        self.head=Node(x)
    
    #新增一筆資料x在y的後面
    def insert (self,y,x):
        flag=False
        temp=self.head
        nodex=Node(x)
        while temp!=None:
            if temp.data==y:
                flag=True
                break
            temp=temp.next
        if flag:
            nodex.next=temp.next
            temp.next=nodex
        else:
            print("連結串列中沒有 ",y)

    #刪除資料x
    def remove(self,x):
        flag=False
        before=self.head
        temp=self.head
        while temp!=None:
            if temp.data==x:
                flag=True
                break
            before=temp
            temp=temp.next
        if flag:
            if temp==self.head:
                self.head=self.head.next
            else: 
                before.next=temp.next
        else:
            print("連結串列中沒有 ",x)
    
    #印出串列中所有資料
    def printNodeList(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.next
        print()

def test():
    li =NodeList()
    li.insertHead(5)
    print(li.head.data)
    li.insert(5,6)
    li.insert(6,9)
    li.printNodeList() 
    li.remove(5)
    li.remove(5)
    li.insert(5,14)
    print(li.head.data)
    li.printNodeList()

test() 
