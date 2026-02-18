NullPointer=-1
Max_size=7

#Node structure
class ListNode:
    def __init__(self):
        self.data=""
        self.Pointer=NullPointer

class ArrayLinkedList:
    def __init__(self):
        self.list=[ListNode() for _ in range(0,Max_size)]
        self.StartPointer=NullPointer
        self.FreeListPTR=0
        self.initialise_list()

    def initialise_list(self):
        self.StartPointer=NullPointer
        self.FreeListPTR=0
        for index in range(Max_size-1):
            self.List[index].Pointer=index+1
        self.List[Max_size-1].Pointer=NullPointer

    def allocate_node(self):
       if self.FreeListPTR== NullPointer:
           print("Overflow:No free nodes available ")
           return NullPointer
       new_node=self.FreeListPTR
       self.FreeListPTR+=self.list[new_node].Pointer
       return new_node

    def free_node(self,node_index):
       self.list[node_index].Pointer=self.FreeListPTR
       self.list[node_index].Data=""
       self.FreeListPTR=node_index

    def insert_at_start(self,value):
        new_node=self.allocate_node()
        if new_node==NullPointer:
            return
        slef.list[new_node].Data=value
        self.list[new_node].Pointer=self.StartPointer
        self.StartPointer=new_node

    def delete_from_start(self):
        if self.StartPointer==NullPointer:
            print("underflow:List is empty ")
            return
        removed_node=self.StartPointer
        self.StartPointer=self.list[removed_node].Pointer
        self.free_node(removed_node)

    def traverse(self):
        index=self.StartPointer
        element=[]
        while index!=NullPointer:
            element.append(self.list[index].Data)
            index=self.list[index].Pointer
        print("->".join(element) if element!=[] else "empty list")

if __name__=="__main__":
    ll=ArrayLinkedList()
    ll.traverse()
    ll.insert_at_start("A")
    ll.insert_at_start("B")
    ll.insert_at_start("C")
    ll.traverse()

    ll.delete_from_start()
    ll.traverse()

    ll.insert_at_start("D")
    ll.traverse()
