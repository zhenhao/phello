__author__ = 'wangzhenhao'


class BTreeNode:
    def __init__(self, ele):
        self.ele = ele
        self.left = None
        self.right = None


class BTree:
    def __init__(self):
        self.root = None

    def insert(self, ele):
        if self.root is None:
            self.root = BTreeNode(ele)
        else:
            self._insert(self.root, ele)

    def _insert(self, node, ele):
        if ele >= node.ele:
            if node.right is None:
                node.right = BTreeNode(ele)
            else:
                self._insert(node.right, ele)
        else:
            if node.left is None:
                node.left = BTreeNode(ele)
            else:
                self._insert(node.left, ele)

    def show(self):
        self._show(self.root)

    def _show(self, node):
        if node is None:
            return
        if node.left is not None:
            self._show(node.left)
        print(node.ele)
        if node.right is not None:
            self._show(node.right)
