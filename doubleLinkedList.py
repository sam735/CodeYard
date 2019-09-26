class DoubleLd():
    def __init__(self,data):
        self.prev = None
        self.next = None
        self.data = data

class DoubleLinklist():
    def __init__(self):
        self.head = None
    def push(self,data:int):
        root = DoubleLd(data)
        root.next = self.head
        if self.head is not None:
            self.head.prev = root  
        self.head = root

    def pop(self,data:int):
        root = self.head
        if root is None:
            return
        if root.data == data:
            self.head = root.next
            return
        
        while root is not None:
            if root.data == data:
                root.prev.next = root.next
            root = root.next

    def display(self):
        root = self.head
        if root is None:        
            return
        else:
            while root is not None:
                print("Data is {}".format(root.data))
                root = root.next

if __name__ == "__main__":
    dlk = DoubleLinklist()
    for i in range(1,6):
        dlk.push(int(input("enter value:")))
    dlk.display()
    dlk.pop(int(input("Enter data to be deleted:")))
    dlk.display()
    dlk.push(int(input("Enter data to be inserted:")))
    dlk.display()