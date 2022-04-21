from node import Node

#Método construtor
class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

 
    def push(self, elem):
        #"""insere um elemento na pilha"""
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size = self._size + 1

    def pop(self):
        #"""remove um elemento no topo da pilha"""
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size = self._size - 1
            return node.data
        raise IndexError("A pilha está vazia!!!")


    def peek(self):
        #"""retorna o topo da pilha sem remover"""
        if self._size > 0:
            return self.top.data
        raise IndexError("A pilha está vazia!!!")

    def len(self):
        #"""Retorna o tamanho da pilha"""
        return self._size

    def __repr__(self):
        r = ""
        pointer = self.top
        while(pointer):
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        return r

    def __str__(self):
         return self.__repr__()

if __name__ == "__main__":
#inserir um elemento
    pilha = Stack()
    pilha.push(3)
    pilha.push(2)
    pilha.push(1)
    pilha.peek()
    print(pilha)


#remover um elemento    
    pilha.pop()
    pilha.pop()
    print(pilha)

#inserir um elemento
    pilha.push(2)
    pilha.push(1)
    print(pilha)

#retornar erro da lista vazia
    pilha.pop()
    print(pilha)
    pilha.pop()
    print(pilha)
    pilha.pop()
    print(pilha)
    pilha.pop()
    print(pilha)