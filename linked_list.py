''' This code for LinkedList is written by Rishu Raj'''


class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        
    def printList(self):
      if self.head is None:
             print("List has no Item")
      temp = self.head
      
      while(temp is not None):
             print (temp.data,end=" ")
             temp=temp.next
      print('\n')
    
    def insert_first(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        
        
    def insert_last(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        n=self.head
        while n.next is not None:
            n=n.next
        n.next=new_node
        
        
    def insert_after(self,x,data):
        n=self.head
        #print(n.next)
        while n is not None:
            if n.data==x:
                break
            n=n.next
        if n is None:
            print("item is not in the list")
        else:
            new_node=Node(data)
            new_node.next=n.next
            n.next=new_node
            
            
    def insert_before(self,x,data):
        if self.head is None:
            print("List has no element")
            return
        if x==self.head.data:
            new_node=Node(data)
            new_node.next=self.head
            self.head=new_node
            return
        n=self.head
        #print(n.next)
        while (n.next is not None):
            if n.next.data == x:
                break
            n=n.next
        if n.next is None:
            print("item not in the list")
        else:
            new_node=Node(data)
            new_node.next=n.next
            n.next=new_node
            
            
    def insert_at(self,index,data):
        if index==1:
            new_node=Node(data)
            new_node.head=self.head
            self.head=new_node
        i=1
        n=self.head
        while(i<index-1 and n is not None):
            n=n.next
            i=i+1
        if n is None:
            print("Index out of Bound")
        else:
            new_node=Node(data)
            new_node.next=n.next
            n.next=new_node
            
            
    def count(self):
        if self.head is None:
                return 0
        n=self.head
        c=0
        while n is not None:
            c=c+1
            n=n.next
        return c
    
    
    def search_data(self,item):
        c=0
        if self.head is None:
            print("List is empty")
            return
        n=self.head
        while n is not None:
            c=c+1
            if n.data==item:
                
                print("Item Found at",c)
                return True
            n=n.next
        print("Item not found")
        return False
    
    
    def make_new_list(self):
        nums=int(input("Enter the number of elements you want to enter"))
        if nums==0:
            return
        for i in range(nums):
            value=int(input("Enter the value of node:"))
            self.insert_last(value)
            
            
    def delete_first(self):
        if self.head is None:
            print("List is empty")
            return
        self.head=self.head.next
        
        
    def delete_last(self):
        if self.head is None:
            print("List is empty")
            return
        n=self.head
        while n.next is not None:
            n=n.next
            n.next=None
            
            
    def delete_element_by_value(self,x):
        if self.head is None:
            print("List is empty")
            return
        if self.head.data == x:
            self.head=self.head.next
            return
        n=self.head
        while n.next is not None:
            if n.next.data==x:
                break
            n=n.next
        if n.next is None:
            print("List is empty")
        else:
            n.next=n.next.next
            
            
    def reverse_list(self):
        prev=None
        n=self.head
        while n is not None:
            next=n.next
            n.next=prev
            prev=n
            n=next
        self.head = prev 
        
        
if __name__=='__main__':
    ch=True
    llist=LinkedList()
    while(ch):
          print("-------------------------")
          print("      Linked List        ")
          print("-------------------------")
          print("Enter your choice in number")
          print("1. Create a node ")
          print("2. Insert at first")
          print("3. Insert at last")
          print("4. Insert after value")
          print("5. Insert before value")
          print("6. Insert at Node")
          print("7. Insert more than one values")
          print("8. Count the number of values in list")
          print("9. Search for Value")
          print("10. Delete first element")
          print("11. Delete last element")
          print("12. Delete element by value")
          print("13. Reverse the linked list")
          print("14. Print the list")
          choice=int(input())
          if(choice==1):
            print("Enter the value:")
            val=int(input())
            llist.head=Node(val)
            print("How many values you want more ?")
            j=int(input())
            for i in range(j):
              print("Enter value",i+1)
              val=int(input())
              llist.insert_last(val)
            
          elif(choice==2):
            print("Enter the value:")
            val=int(input())
            llist.insert_first(val)
            
          elif(choice==3):
            print("Enter the value:")
            val=int(input())
            llist.insert_last(val)
            
          elif(choice==4):
            print("Enter the value after which you want to input:")
            val=int(input())
            print("Enter the value to be input:")
            val2=int(input())
            llist.insert_after(val,val2)
            
          elif(choice==5):
            print("Enter the value before which you want to input:")
            val=int(input())
            print("Enter the value to be input:")
            val2=int(input())
            llist.insert_before(val,val2)
            
          elif(choice==6):
            print("Enter the Node Number at which you want to input:")
            val=int(input())
            print("Enter the value to be input:")
            val2=int(input())
            llist.insert_at(val,val2)
            
            
          elif(choice==7):
            llist.make_new_list()
            
            
          elif(choice==8):
            print("The number of items in the list are:",llist.count())
            
            
          elif(choice==9):
            print("Enter the value you want to search:")
            val=int(input())
            llist.search_data(val)
            
            
          elif(choice==10):
            llist.delete_first()
            
            
          elif(choice==11):
            llist.delete_last()
            
            
          elif(choice==12):
            print("Enter the value you want to delete")
            val=int(input())
            llist.delete_element_by_value(val)
            print("Value deleted successfully !")
            print("Enter 14 to check")
            
            
          elif(choice==13):
            llist.reverse_list()
            
            
          elif(choice==14):
            llist.printList()
            
            
          else:
            print("Value entered is not correct.")
            print("Retry ! Exit")
            ch=False
    
