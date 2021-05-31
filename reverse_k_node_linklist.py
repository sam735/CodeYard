
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class Linklist():
    start = None
    def __init__(self):
        self.rv_start = None
    
    def insert(self,data):
        ptr = Node(data)
        ptr.next = Linklist.start
        Linklist.start = ptr

    # def get_k_partition_ptr(self,k):
    #     temp_start = Linklist.start
    #     prev_ptr = temp_start
    #     count = 0
    #     while count <= k:
    #         temp_start = temp_start.next
    #     return prev_ptr,temp_start
    
    # def reverse_in_group(self,start,end):
    #     temp_start = Linklist.start
    #     while start <= end:
    #         tmp = start
    #         tmp_next = start.next
    #         tmp.next  = None
    #         tmp_next.next = tmp
    def reverse_in_group(self,head,k):
        if head is None:
            return
        count = 0
        current = head
        start = None
        while current is not None and count <k:
            tmp = current
            current = current.next
            tmp.next = start
            start = tmp
            count += 1
        if current is not None:
            head.next = self.reverse_in_group(current,k)
        return start


    def reverse_linked_list(self):
        ptr = Linklist.start
        while ptr is not None:
            tmp = ptr
            ptr = ptr.next
            tmp.next = self.rv_start
            self.rv_start = tmp

    def display(self,ptr=None):
        if ptr:
            temp_start = ptr
        elif  self.rv_start is not None:
            temp_start = self.rv_start
        else:
            temp_start = Linklist.start
        while temp_start is not None:
            print(temp_start.data,sep=' ')
            temp_start = temp_start.next

if __name__ == "__main__":
    linklist = Linklist()
    arr = [8,7,6,5,4,3,2,1]
    for elem in arr:
        linklist.insert(elem)
    linklist.display()
    ptr = linklist.reverse_in_group(Linklist.start,3)
    # linklist.reverse_linked_list()
    print('After reversing list',end='\n')
    linklist.display(ptr)
    

    
