import queue
import sys
sys.setrecursionlimit(10**6)

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

count = 0
def getCount(root, count):
    if root == None:
        return True

    left_val = getCount(root.left, count)
    right_val = getCount(root.right, count)

    if left_val == False or right_val == False :
        return False
    if root.left and root.data != root.left.data:
        return False
    if root.right and root.data != root.right.data:
        return False
    
    count[0] += 1
    return True
     

def countUnivalTrees(root):
    count = [0]
    getCount(root, count)
    return count[0]


def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    
    if length<=0 or levelorder[0]==-1:
        return None
    
    root = BinaryTreeNode(levelorder[index])
    index += 1
    
    q = queue.Queue()
    q.put(root)
    
    while not q.empty():
        
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        
        if leftChild != -1:
            
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
            
        rightChild = levelorder[index]
        index += 1
        
        
        if rightChild != -1:
            
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
            
            
    return root
    
t = int(input())
while t >0:
    li = [int(i) for i in input().split()]
    root = buildLevelTree(li)
    print(countUnivalTrees(root))
    t = t -1
