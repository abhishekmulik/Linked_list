##singlyLinkedList

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linked_list:
    def __init__(self):
        self.start=None
        self.size=0

    def delFirst(self):
        if self.start==None:
            print('empty ll')
        else:
            self.start=self.start.next
            self.size-=1
    
    def __len__(self):
        return self.size

    def insertLast(self,value):
        newNode=Node(value)
        if self.start==None:
            self.start=newNode
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.next=newNode
        self.size+=1
    
    def view(self):
        if self.start==None:
            print('empty')
        else:
            temp=self.start
            while temp.next!=None:
                print(temp.data,end=' ')
                temp=temp.next
                
    
        
            

l=linked_list()
for i in range(5):
    l.insertLast(i)
print('the linked is:')
l.view()
l.delFirst()
print()
print('After deleting first item')
l.view()
print()
print('lenght is',len(l))

        
    

        


