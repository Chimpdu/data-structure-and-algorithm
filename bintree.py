COUNT = [10]
def print2DUtil(root, space):
 
    # Base case
    if (root == None):
        return
 
    # Increase distance between levels
    space += COUNT[0]
 
    # Process right child first
    print2DUtil(root.right, space)
 
    # Print current node after space
    # count
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(root.key)
 
    # Process left child
    print2DUtil(root.left, space)
 
# Wrapper over print2DUtil()
 
 
def print2D(root):
 
    # space=[0]
    # Pass initial space count as 0
    print2DUtil(root, 0)

class Node:
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.mirror_1 = False

    def search(self, key):
        return self.search_help(self.root, key)
    
    def search_help(self, node, key):
        if not self.mirror_1:
            if not node: # The node is not in the tree
                return False
            elif node.key > key:
                return self.search_help(node.left, key)
            elif node.key < key:
                return self.search_help(node.right, key)
            return True # The node stores the key
        else:   
            if not node: # The node is not in the tree
                return False
            elif node.key < key:
                return self.search_help(node.left, key)
            elif node.key > key:
                return self.search_help(node.right, key)
            return True # The node stores the key

    def insert(self, key: int):
        if self.root == None:
            self.root = Node(key)
        elif self.search(key) == True:
            return
        else:
            self.insert_help(self.root, key)

    def insert_help(self, node, key: int):
        if not self.mirror_1:
            if key > node.key:
                if node.right == None:
                    node.right = Node(key)
                else:
                    self.insert_help(node.right, key)
            elif key < node.key:
                if node.left == None:
                    node.left = Node(key)
                else:
                    self.insert_help(node.left, key)
        else:
            if key < node.key:
                if node.right == None:
                    node.right = Node(key)
                else:
                    self.insert_help(node.right, key)
            elif key > node.key:
                if node.left == None:
                    node.left = Node(key)
                else:
                    self.insert_help(node.left, key)
    def preorder(self):
        content_list = []
        self.preorder_help(self.root, content_list)
        string = ""
        for i in range(len(content_list)):
            string += str(content_list[i]) + " "
        string.rstrip(" ")
        print(string)

    def preorder_help(self, node, content_list): 
        
        if (node != None):
            content_list.append(node.key) 
            self.preorder_help(node.left, content_list)
            self.preorder_help(node.right, content_list)
        else: return 

    def remove(self, key: int):
        """ hidden test not passed, see whether remove root node is implemented correctly(more test cases) also inspect the whole remove method """
        result = []
        if self.search(key)==False:
            return
        if self.root.key == key:
            if self.root.left == None and self.root.right == None:
                self.root = None
            elif self.root.left == None or self.root.right == None:
                if self.root.left != None:
                    self.root = self.root.left
                else:
                    self.root = self.root.right
            else:
                if self.mirror_1 == True:
                    max = self.left_max(self.root.right)
                    left_max_value = max.key
                    self.remove(max.key)
                    self.root.key = left_max_value
                else:
                    max = self.left_max(self.root.left)
                    left_max_value = max.key
                    self.remove(max.key)
                    self.root.key = left_max_value
        else:
            self.remove_help(self.root, key, result)
            if result == None:
                return 
            else:
                parent_node = result[0]
                child_node = result[1]
                if child_node.left == None and child_node.right == None:
                    if parent_node.left and parent_node.left.key == child_node.key:
                        parent_node.left = None
                    else:
                        parent_node.right = None
                elif child_node.left == None or child_node.right == None:
                    if parent_node.left and parent_node.left.key == child_node.key:
                        if child_node.left != None:
                            parent_node.left = child_node.left
                        else:
                            parent_node.left = child_node.right
                    elif parent_node.right and parent_node.right.key == child_node.key:
                        if child_node.left != None:
                            parent_node.right = child_node.left
                        else:
                            parent_node.right = child_node.right
                
                else:
                    left_max = self.left_max(child_node.left)
                    left_max_value = left_max.key
                    self.remove(left_max.key)
                    child_node.key = left_max_value
                
    def remove_help(self, node, key: int, result: list):
        child_node = self.remove_help2(node, key)
        parent_node= self.remove_help1(node, key)
        result.append(parent_node)
        result.append(child_node)
    
    def remove_help1(self, node, key: int):
        if not self.mirror_1:
            if not node: 
                return None  
            if ((node.left and node.left.key == key) or (node.right and node.right.key == key)):
                return node  
            elif ((node.left or node.right) and  node.key > key):
                return self.remove_help1(node.left, key)
            elif ((node.left or node.right) and  node.key < key):
                return self.remove_help1(node.right, key)
            else: 
                return None
        else:
            if not node: 
                return None  
            if ((node.left and node.left.key == key) or (node.right and node.right.key == key)):
                return node  
            elif ((node.left or node.right) and  node.key < key):
                return self.remove_help1(node.left, key)
            elif ((node.left or node.right) and  node.key > key):
                return self.remove_help1(node.right, key)
            else: 
                return None
    def remove_help2(self, node, key: int):
        if not self.mirror_1:
            if not node: 
                return None  
            if node.key == key:
                return node  # Node found, return the node
            elif node.key > key:
                return self.remove_help2(node.left, key)
            else:
                return self.remove_help2(node.right, key)
        else:
            if not node: 
                return None  
            if node.key == key:
                return node  # Node found, return the node
            elif node.key < key:
                return self.remove_help2(node.left, key)
            else:
                return self.remove_help2(node.right, key)
            
    
    def left_max(self, node):
        if not node:
            return None
    
        while node.right:
            node = node.right
    
        return node

    """ def left_max(self, node):
        max = node
        return self.left_max_help(max, node)
    
    def left_max_help(self, max, node):
        if not self.mirror_1:
            if node == None:
                return
            elif node.key > max.key:
                max = node
            self.left_max_help(max, node.left)
            self.left_max_help(max, node.right)
            return max
        else:
            if node == None:
                return
            elif node.key < max.key:
                max = node
            self.left_max_help(max, node.left)
            self.left_max_help(max, node.right)
            return max
 """
    def postorder(self):
        content_list = [] # list is more like pass by reference
        self.postorder_help(self.root, content_list)
        string = ""
        for i in range(len(content_list)):
            string += str(content_list[i]) + " "
        string.rstrip(" ")
        print(string)

    def postorder_help(self, node, content_list): 
        
        if (node != None): 
            self.postorder_help(node.left, content_list)
            self.postorder_help(node.right, content_list)
            content_list.append(node.key)
        else: return 
    def inorder(self):
        content_list = [] # list is more like pass by reference
        self.inorder_help(self.root, content_list)
        string = ""
        for i in range(len(content_list)):
            string += str(content_list[i]) + " "
        string.rstrip(" ")
        print(string)

    def inorder_help(self, node, content_list): 
        
        if (node != None): 
            self.inorder_help(node.left, content_list)
            content_list.append(node.key)
            self.inorder_help(node.right, content_list)
        else: return 

    def breadthfirst(self):
        not_searched = [self.root]
        searched = []
        self.breadthfirst_help(not_searched, searched)
        string = ""
        for i in range(len(searched)):
            string += str(searched[i].key) + " "
        string.rstrip(" ")
        print(string)

    def breadthfirst_help(self, not_searched:list, searched:list):
        tempo_list = []
        
        for i in range(len(not_searched)):
            searched.append(not_searched[i])
            if (not_searched[i].left):
                tempo_list.append(not_searched[i].left)
            if (not_searched[i].right):
                tempo_list.append(not_searched[i].right)
        if tempo_list == []:
            return
        else:
            self.breadthfirst_help(tempo_list, searched)
    def mirror(self):
        self.mirror_1 = not self.mirror_1
        self.mirror_help(self.root)
    def mirror_help(self, node):
        #algorithm: node = None: return; move to the left; move to the right; swap  
        if node == None:
            return
        else:
            self.mirror_help(node.left)
            self.mirror_help(node.right)
            node.left, node.right = node.right, node.left




 
 


if __name__ == "__main__":
    tree = BST()

    for num in (14, 19, 13, 23, 12, 17, 16, 10, 15, 11, 22, 28, 30, 25, 20):
        tree.insert(num)

    for num in (20, 25, 11, 29, 14):
        tree.remove(num)

    tree.preorder()  
