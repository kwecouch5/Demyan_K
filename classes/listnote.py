class  ListNode:
    def __init__(self,data=0):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def __str__(self):
        current_node=self.head
        result=""
        while current_node:
            result=result+str(current_node.data)+","
            current_node=current_node.next
        return result[:-1:]

    def insert_in_begin(self,data):
        new_node=ListNode(data)
        if self.head is None:
            self.head=new_node
            return
        else:
            new_node.next=self.head
            self.head=new_node
            return

    def insert_in_end(self,data):
        new_node=ListNode(data)
        current_node=self.head
        if self.head is None:
            self.head=new_node
            return
        else:
            while current_node.next is not None:
                current_node=current_node.next
            current_node.next=new_node
            return

    def del_first(self):
        if self.head is None:
            return None
        else:
            current_node=self.head
            current_node_1=current_node.next
            self.head=current_node_1
            return current_node.data

    def del_last(self):
        if self.head is None:
            return None
        else:
            current_node=self.head
            current_node_1=current_node
            while current_node.next is not None:
                current_node_1=current_node
                current_node=current_node.next
            current_node_1.next=None
            return current_node.data
    def insert_by_index(self,data,ind):
        new_node = ListNode(data)
        if self.head is None:
            self.head=new_node
            return
        else:
            if ind == -1:
                current_node = self.head
                self.head=new_node
                new_node.next=current_node
                return
            elif ind==0:
                current_node=self.head
                current_node_1=current_node.next
                current_node.next=new_node
                new_node.next=current_node_1
                return
            current_node=self.head
            a=0
            while ind!=a and current_node.next is not None:
                current_node=current_node.next
                a+=1
                current_node_1=current_node.next
            current_node.next=new_node
            new_node.next=current_node_1
            return
    def del_by_index(self,ind):
        if self.head is None:
            return None
        a=0
        current_node=self.head
        while current_node.next is not None:
            current_node=current_node.next
            a+=1
        if ind>a:
            return None
        a=0
        current_node_1=current_node
        while ind!=a:
            current_node_1=current_node
            current_node=current_node.next
            a+=1
        current_node_1.next=current_node.next
        return current_node
    def is_averge_el(self):
        if self.head is None:
            return None
        current_node=self.head
        count=0
        while current_node.next is not None:
            current_node=current_node.next
            count+=1
        if count%2==1:
            count=count//2+1
        else:
            count=count//2-1
        current_node=self.head
        while count!=0:
            current_node=current_node.next
            count+=-1
        print(current_node.data)
        return
    def is_avg_fast(self):
b=LinkedList()
b.insert_in_begin('dd')
b.insert_in_begin('ss2')
b.insert_in_begin('s633s')
b.insert_in_begin('s34s')
b.insert_in_begin('ss3')
b.insert_in_begin('s3s')
b.insert_in_begin('s000s')
print(b)
b.is_averge_el()