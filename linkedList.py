class Node():
    def __init__(self,data:int, next_node = None):
        self.data = data
        self.next_node = next_node

def push(root):
    element = int(input('Enter  the element:'))
    node = Node(element)
    node.next_node = root
    return node
    
def display(root):
    if(root == None):
        return
    print(root.data)
    display(root.next_node)

def swapEveryTwoNodesForOddinput(root):
    count = 0
    begin = None
    itr_root = None
    while(root != None):
        #import pdb; pdb.set_trace()
        prev_root = itr_root
        tmp = root.next_node
        root.next_node = root.next_node.next_node
        tmp.next_node = root
        itr_root = root
        root = root.next_node
        count += 1
        if(count == 1):
            begin = tmp

        if(count >1):
            prev_root.next_node = tmp
    return begin

class Bst():
    def __init__(self,data:int, left=None, right = None):
        self.data = data
        self.left = left
        self.right = right


push_bst(root)


if __name__ == "__main__":
    root = None
    length = 0
    while(length < 8):
        root = push(root)
        length += 1
    display(root)
    root = swapEveryTwoNodesForOddinput(root)
    print('Dispaly after swap ')
    display(root)