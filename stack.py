
class Stack:
    def __init__(self):
        self.stack = []

# проверка стека на пустоту. Метод возвращает True или False.
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

# добавляет новый элемент на вершину стека. Метод ничего не возвращает.
    def push(self, item):
        self.stack.append(item)

# удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
    def pop(self):
        removed = self.stack.pop()
        return removed

# возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
    def peek(self):
        top_element = self.stack[-1]
        return top_element

# возвращает количество элементов в стеке.
    def size(self):
        return len(self.stack)