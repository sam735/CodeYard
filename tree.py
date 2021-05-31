class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Utils():
    def __init__(self):
        pass

    def insert(self, data, root):
        if root is None:
            root = Node(data)
        if root.data < data:
            root.right = self.insert(data, root.right)
        if root.data > data:
            root.left = self.insert(data, root.left)
        return root

    def inorder_display(self, root):
        if root is None:
            return
        self.inorder_display(root.left)
        print(root.data)
        self.inorder_display(root.right)
    
    def get_minimum(self,root):
        tmp = root.right
        while tmp.left is not None:
            tmp = tmp.left
        return tmp
    
    def pre_order(self,root):
        if root is None:
            return
        print(root.data)
        self.pre_order(root.left)
        self.pre_order(root.right)
    
    def post_order(self,root):
        if root is None:
            return
        self.pre_order(root.left)
        self.pre_order(root.right)
        print(root.data)

    def delete(self,root,data):
        if root is None:
            return root
        if root.data > data:
            root.left = self.delete(root.left,data)
        elif root.data < data:
            root.right = self.delete(root.right,data)
        else:

            if root.right is None:
                tmp = root.left
                root = None
                return tmp
            elif root.left is None:
                tmp = root.right
                root = None
                return tmp
            
            tmp = self.get_minimum(root)
            root.data = tmp.data
            self.delete(root.right,tmp.data)
        return root
    
    def get_lca(self,root,n1,n2):
        if root is None:
            return None
        
        if root.data > n1 and root.data > n2:
            return self.get_lca(root.left,n1,n2)
        
        elif root.data < n1 and root.data < n2:
            return self.get_lca(root.right,n1,n2)
        
        else:
            return root.data
        
            

            
                



class Bst():
    def __init__(self):
        self.root = None
        self.utils = Utils()

    def insert(self, data):
        self.root = self.utils.insert(data, self.root)
    
    def delete(self,data):
        self.root = self.utils.delete(self.root,data)

    def inorder_display(self):
        self.utils.inorder_display(self.root)
    
    def pre_order_traversal(self):
        self.utils.pre_order(self.root)
    
    def post_order_traversal(self):
        self.utils.post_order(self.root)
    
    def get_lca(self,n1,n2):
        return self.utils.get_lca(self.root,n1,n2)


if __name__ == '__main__':
    elem = [20, 8, 22, 4, 12, 10, 14]
    bst = Bst()
    for el in elem:
        bst.insert(el)
    # print('After deletion .........')
    print(bst.get_lca(10,22))
    
