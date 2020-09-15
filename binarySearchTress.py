#brinary saarch tree

class bst():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    
#insert inode
def insertNode(root,newNode):
        if newNode.data > root.data and root.right is None:
            print("insert right")
            root.right = newNode
            return
        if newNode.data < root.data and root.left is None:
            print("insert left")
            root.left = newNode
            return
        
        #traverse
        traverse = True
        while traverse:
            if newNode.data > root.data and root.right is not None:
                print(root.data,'right')
                root = root.right
            if newNode.data < root.data and root.left is not None:
                print(root.data,'left')
                root = root.left
            else :
                traverse = False     
        if newNode.data > root.data:
            print(root.data)
            root.right = newNode
        if newNode.data < root.data:
            print(root.data)
            root.left = newNode
        return    


#traverse breath first traverse

def breathFirstTraverse(root):
    print("breath first")
    traverse = True
    while traverse:
        if root.left is not None :
            print(root.data)
            root = root.left
        else:
            traverse = False





if __name__ == "__main__":
    print("Insert A Node")
    firstNode= int(input("enter node"))
    rootNode = bst(firstNode)
    print(rootNode.data)
    userPromt='y'
    while userPromt == 'y':
        data=int(input("Enter Node Data"))
        # print(data)
        newNode = bst(data)
        insertNode(rootNode,newNode)
        search = input("Doy you wnat to search")
        if search == 'y':
             breathFirstTraverse(rootNode)
        userPromt =  input("Do you wnat to conrine")

