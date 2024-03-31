class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Metodo para adicionar elementos a fila
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    # Metodo para remover elemento da fila
    def dequeue(self):
        if self.front is None:
            return None
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return temp.data

    # Metodo para verificar se a fila esta vazia
    def is_empty(self):
        return self.front is None

    # Metodo para visualizar o primeiro elemento da fila
    def peek(self):
        if self.front is None:
            return None
        return self.front.data

    # Metodo para exibir a fila
    def display_queue(self):
        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Criando uma instancia da fila
q = Queue()

# Adicionando elementos a fila
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Exibindo o estado atual da fila
print("Estado atual da fila:")
q.display_queue()

# Adicionando mais tres elementos a fila
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)

# Exibindo o estado atual da fila apos adicionar mais elementos
print("\nEstado atual da fila apos adicionar 4, 5 e 6:")
q.display_queue()

# Removendo dois elementos da fila
q.dequeue()
q.dequeue()

# Exibindo o estado atual da fila apos remover elementos
print("\nEstado atual da fila apos remover dois elementos:")
q.display_queue()

# Visualizando o primeiro elemento da fila apos as remoçoes
print("\nPrimeiro elemento da fila apos as remoçoes:", q.peek())

# Verificando se a fila esta vazia
if q.is_empty():
    print("\nFila esta vazia")
else:
    print("\nFila nao esta vazia")
