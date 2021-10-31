#binary tree diameter



class BinaryTree():
    def __init__(self,data):
        self.value = data
        self.left = None
        self.right = None

# class bst():
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None




class Tree():
    def __init__(self):
        self.root = 'None'

    #get the root of the binary tree
    def showRooot(self):
        return self.root
    
    def addNode(self,tree,value):
        #traverse oveer the tree
        node = tree 
        # print(node.value)
        traverse = True
        while traverse:
            if(node.value > value and node.right is not None):
                node = node.right
            elif (node.value <= value  and node.left is not None):
                node = node.left
            else :
                traverse = False

        #if node valueis gratre then add left
        if(node.value <= value):
            node.left = BinaryTree(value)
        else :
            node.right = BinaryTree(value)

    def breadthfirstTraverse(self,tree):

        traverseArray = [tree]
        while traverseArray:
            node = traverseArray.pop()
            print(node.value)
            binaryTreeDaimeter(node)
            if(node.left is not None):
                traverseArray.append(node.left)
            if (node.right is not None):
                traverseArray.append(node.right)




def binaryTreeDaimeter(tree):
    # print(tree.right.value)
    maxnumber = 0
    left  = depth(tree,{'no':0})
    right = depthright(tree,{'no':0})
    maxnumber = max(maxnumber,(left['no'] + right['no']))
    print("max",maxnumber)

def depth(tree,count):
    if(tree):
        print("enter",count,tree.value)
        count['no'] = count['no'] + 1 
        depth(tree.left,count)
    return count


def depthright(tree,count):
    if(tree):
        print("enter right",count,tree.value)
        count['no'] = count['no'] + 1 
        depthright(tree.right,count)
    return count


   

    





print("this is the start")
btree = BinaryTree(1)
# print(btree.value)
tree = Tree()
# tree.addNode(btree,3) 
# tree.addNode(btree,2) 
# tree.addNode(btree,7)
# tree.addNode(btree,4) 
# tree.addNode(btree,8) 
# tree.addNode(btree,5) 
# tree.addNode(btree,9)  
# tree.addNode(btree,6)  
btree.left = BinaryTree(3) 
btree.right = BinaryTree(2) 
btree.left.left = BinaryTree(7)
btree.left.right = BinaryTree(4)
btree.left.right.right = BinaryTree(5)
btree.left.right.right.right = BinaryTree(6)
btree.left.left.left = BinaryTree(8)
btree.left.left.left.left = BinaryTree(9)
tree.breadthfirstTraverse(btree)
# binaryTreeDaimeter(btree)