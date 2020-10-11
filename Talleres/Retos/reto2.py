class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self, head):
        self.head = head

    def length(self):
        dato = self.head
        if dato is not None:
            cont = 1

            while dato.next is not None:
                cont += 1
                dato = dato.next
            return cont
        else:
            return 0

    def insert(self, data, position):
        newNode = Node(data)

        if position == 0:
            newNode.next = Lista.head
            Lista.head = newNode
        else:
            dato = Lista.head
            a = 1
            while dato.next is not None and a < position:
                dato = dato.next
                a += 1
            newNode.next = dato.next
            dato.next = newNode

    def Aveces(self, a):
        if a >= self.length():
            a = a % self.length()

        i = 1
        while i <= a:
            dato = self.head
            while dato.next.next is not None:
                dato = dato.next

            dato.next.next = self.head
            self.head = dato.next
            dato.next = None
            i += 1

    def showList(self):
        dato = Lista.head
        while dato is not None:
            print(dato.data, end = ", ")
            dato = dato.next   
        print()
            
Lista = Stack(Node(1))

for i in range(2,6):
    Lista.insert(i, i-1)


print("Lista:")
Lista.showList()

Lista.Aveces(10000003)
print("Lista despues de 10000003 pasadas:")
Lista.showList()


#pagina de la que me vace https://www.geeksforgeeks.org/implement-a-stack-using-singly-linked-list/