#node Structure
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
#class Linked List
class DlinkedList:
    def __init__(self):
        self.head=None
    #create dobly linked list
    def createDLL(self,value):
        new_node=Node(value)
        self.head=new_node
        print("The doubly linked list has been created.")
    #Add new element at the end of the list
    def append(self,new_Element):
        new_node=Node(new_Element)
        temp=self.head
        if(temp==None):
            self.head=new_node
            return
        else:
            while(temp.next !=None):
                temp=temp.next
            temp.next=new_node
            new_node.prev=temp
    #Delete an element at the given position
    def deleteFront(self):
        if(self.head !=None):
            temp=self.head
            print("Node value deleted is ",temp.data)
            self.head=self.head.next
        temp=None
        if(temp!=None):
            self.head.prev=None
    #display the content of the list
    def printList(self):
        temp=self.head
        if(temp !=None):
            print("The last contains:",end=" ")
            while(temp!=None):
                print(temp.data,end=" <=> ")
                temp=temp.next
            print()
        else:
            print("The list is Empty.")
    #search an element 
    def Search(self,key):
        position=0
        temp=self.head
        while temp is not None:
            position=position+1
            if temp.data == key:
                return position
            temp = temp.next
            return -1
#test the code
MyList=DlinkedList()
#create a node
MyList.createDLL(5)
MyList.printList()
print("Enter 1 to Search\nEnter 2 to Delete\nEnter 3 to append\nEnter 4 to stop")
choice=int(input("Input your Choice:"))
while(choice==1 or choice==2 or choice==3):
    if(choice==1):
        key=int(input("Enter key to search:"))
        print("Search for ",key)
        pos=MyList.Search(key)
        if pos==-1:
            print(str(key)+" is not found")
        else:
            print(str(key)+" is found at position "+str(pos))
    elif(choice==2):
        MyList.deleteFront()
        MyList.printList()
    elif(choice==3):
        value=int(input("Enter the node value:"))
        MyList.append(value)
        MyList.printList()
    else:
        break
    choice=(int(input("\nInput your choice:")))
print("-----end-----")