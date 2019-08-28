from queue import SimpleQueue


class Bst():
    def __init__(self, data: int, l=None, r=None):
        self.data = data
        self.l = l
        self.r = r


def insert_bst(data: int, root=None):
    if root is None:
        root = Bst(data)
        return root
    if(root.data > data):
        root.l = insert_bst(data, root.l)
    if root.data < data:
        root.r = insert_bst(data, root.r)
    return root


def in_oredr_traversal(root=None):
    if root is None:
        return
    in_oredr_traversal(root.l)
    print(root.data)
    in_oredr_traversal(root.r)


def pre_order_traversal(root=None):
    if root is None:
        return
    print(root.data)
    in_oredr_traversal(root.l)
    in_oredr_traversal(root.r)


def post_order_traversal(root=None):
    if root is None:
        return
    post_order_traversal(root.l)
    post_order_traversal(root.r)
    print(root.data)


def level_order_traversal(root=None):
    if root is None:
        return
    Que = SimpleQueue()
    Que.put(root)
    while Que.empty() is False:
        node = Que.get()
        print(node.data)
        if node.l is not None:
            Que.put(node.l)
        if node.r is not None:
            Que.put(node.r)


if __name__ == '__main__':
    root = None
    for i in range(1, 5):
        n = int(input('Enter data:'))
        root = insert_bst(n, root)
    print('Inorder traversal')
    in_oredr_traversal(root)
    print('preorder traversal')
    pre_order_traversal(root)
    print('postorder traversal')
    post_order_traversal(root)
    print('levelorder traversal')
    level_order_traversal(root)