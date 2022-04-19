class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
    
class linked_list:
    def __init__(self):
        self.head=node()

    def append(self,data):
        cur=self.head
        while cur.next!=None:
            cur=cur.next
        cur.next=node(data)

    def length(self):
        cur=self.head
        total=0
        while cur.next!=None:
            cur=cur.next
            total+=1
        return total
    
    def display(self):
        elems=[]
        cur=self.head
        while cur.next!=None:
            cur=cur.next
            elems.append(cur.data)
        print(elems)
    
    def get(self,index):
        if index>=self.length():
            print("error: 'get' index out of range")
            return None
        cur_index=0
        cur=self.head
        while True:
            cur=cur.next
            if cur_index==index:
                return cur.data
            cur_index+=1
    
    def erase(self,index):
        if index>=self.length():
            print("error: getindex out of range")
            return 
        cur=self.head
        cur_index=0
        while True:
            lastnode=cur
            cur=cur.next
            if cur_index==index:
                lastnode.next=cur.next
                return
            cur_index+=1


#lets try creating a list and perform different operations using above defined functions.
a=linked_list() # initialize list

#now let's add new nodes
a.append(5)
a.append(8)
a.append(90)

#now, let's print the length of list
print(a.length())

#display the elements of the list
a.display()

#again add more nodes
a.append(15)
a.append(38)
a.append(70)

#again print the new length and display the elements
print(a.length())
a.display()

#get the element present at a particular index
print(a.get(4))

#deleting(removing) a node from the list
a.erase(3)
#again diplay the elements
a.display()
