class Node:

    def __init__(self, root):

        self.root = root
        self.left = None
        self.right = None

    def buildTree(self, root):

        if self.root:
            if root < self.root:
                if self.left is None:
                    self.left = Node(root)
                else:
                    self.left.buildTree(root)
            elif root > self.root:
                if self.right is None:
                    self.right = Node(root)
                else:
                    self.right.buildTree(root)
        else:
            self.root = root

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.root),

        if self.right:
            self.right.PrintTree()

    def maxDepth(self, root):

        if root:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        else:
            return 0

# l = [1,2,3,4,5] #1 2 4 5 3
# sol = Node()
# print(sol.preOrder(l))

root = Node(1)
root.buildTree(2)
root.buildTree(3)
root.buildTree(4)
root.buildTree(5)

# print(root.PrintTree())
print(root.maxDepth(root))


