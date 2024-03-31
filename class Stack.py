class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

def reverse_string(input_string):
    stack = Stack()
    for char in input_string:
        stack.push(char)
    
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string


input_string = input("Digite uma string: ")
print("String invertida:", reverse_string(input_string)) 
 