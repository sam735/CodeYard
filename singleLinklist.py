class LinkedList():
    def __init__(self,data):
        self.next = None
        self.data = data

class Link():
    def __init__(self):
        self.head = None

    def push(self,data:int):
        root = LinkedList(data)
        root.next = self.head
        self.head = root

    def display(self):
        root = self.head
        if root is None:
            return
        while root is not None:
            print(root.data)
            root = root.next

    def delete(self,data):
        root = self.head
        prv = None
        if root is None:
            return
        
        if root.data == data:
            self.head = root.next
            return
        while root is not None:
            if root.data == data:
                prv.next = root.next
            prv = root
            root = root.next
    def reverse(self):
        root = self.head
        #import pdb; pdb.set_trace()
        if root is None:
            return
        final = None
        while (root is not None):
            tmp = root.next
            root.next = final
            final = root
            root = tmp
        self.head = final




if __name__ == "__main__":
    lst = Link()
    for i in range(1,6):
        lst.push(int(input("enter value:")))
    lst.display()
    lst.reverse()
    print('Element after reverse')
    lst.display()
    lst.delete(int(input("Enter data to be deleted:")))
    lst.display()
    lst.push(int(input("Enter data to be inserted:")))
    lst.display()