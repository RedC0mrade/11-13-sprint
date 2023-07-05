# 88835324
from operator import add, floordiv, mul, sub


class Stack:

    def __init__(self):
        """Параметры Стэка"""
        self.stack = []

    def push(self, data: int):
        """Добавление элемента"""
        return self.stack.append(data)

    def pop(self):
        """Возващение и удаление последнего элемента"""
        if len(self.stack) == 0:
            return None
        return self.stack.pop()


def polish_notation(notation: str):
    """Решение польской нотации"""
    stack = Stack()
    operators = {'+': add, '-': sub, '*': mul, '/': floordiv}
    for i in notation:
        if i in operators:
            last_data = stack.pop()
            pre_last_data = stack.pop()
            result = operators[i](pre_last_data, last_data)
            stack.push(result)
        else:
            stack.push(int(i))
    return stack.pop()


def main():
    """Основная функция"""
    notation = input().split()
    print(polish_notation(notation))


if __name__ == '__main__':
    main()
