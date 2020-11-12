class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildtree(inorder, preorder, instrt, inend):
    if instrt > inend:
        return None
    Nodo = Node(preorder[buildtree.preIndex])
    buildtree.preIndex += 1
    if instrt == inend:
        return Nodo
    inindex = search(inorder, instrt, inend, Nodo.data)
    Nodo.left = buildtree(inorder, preorder, instrt, inindex - 1)
    Nodo.right = buildtree(inorder, preorder, inindex + 1, inend)
    return Nodo

def search(arr, start, end, value):
    for i in range(start, end + 1):
        if arr[i] == value:
            return i

def inorden(i):
    if i is None:
        return None
    else:
        inorden(i.left)
        print(i.data, end=' ')
        inorden(i.right)

def preorden(i):
    if i is None:
        return None
    else:
        print(i.data, end=' ')
        preorden(i.left)
        preorden(i.right)

preord = ['G', 'E', 'A', 'I', 'B', 'M', 'C', 'L', 'D', 'F', 'K', 'J', 'H']
inord = ['I', 'A', 'B', 'E', 'G', 'L', 'D', 'C', 'F', 'M', 'K', 'H', 'J']

buildtree.preIndex = 0
arbol = buildtree(inord, preord, 0, len(inord) - 1)
inorden(arbol) 
print(" ")
preorden(arbol)  
print(" ")