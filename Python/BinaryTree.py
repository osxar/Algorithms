class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self,rootValue):
        self.root = Node(rootValue)

    
    def preorderDFS(self,node,result):

        if(node is None):
            return None

        result.append(node.value)
        self.preorderDFS(node.left,result)
        self.preorderDFS(node.right,result)

        return result


    def inorderDFS(self,node,result):

        if(node is None):
            return None

        self.inorderDFS(node.left,result)
        result.append(node.value)
        self.inorderDFS(node.right,result)

        return result

    
    def postorderDFS(self,node,result):

        if(node is None):
            return None

        self.postorderDFS(node.left,result)
        self.postorderDFS(node.right,result)
        result.append(node.value)

        return result

    def levelorderBFS(self,node):
        queue = []
        result = []

        queue.append(node)

        while(len(queue)):

            if(queue[0].left):
                queue.append(queue[0].left)
            
            if(queue[0].right):
                queue.append(queue[0].right)
            
            result.append(queue.pop(0).value)

        return result





Bt = BinaryTree(3)

Bt.root.left = Node(4)
Bt.root.left.left = Node(6)
Bt.root.left.right = Node(7)

Bt.root.right = Node(5)
Bt.root.right.left = Node(8)
Bt.root.right.right = Node(9)

# result = []

print(Bt.levelorderBFS(Bt.root))