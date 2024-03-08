# 88863240
from operator import add, floordiv, mul, sub


class EmptyStackError(Exception):
    """Empty stack error."""


class Stack:

    def __init__(self):
        """Параметры Стэка"""
        self.stack = []

    def push(self, data: int) -> None:
        """Добавление элемента"""
        return self.stack.append(data)

    def pop(self) -> int:
        """Возващение и удаление последнего элемента."""
        if not self.stack:
            raise EmptyStackError
        return self.stack.pop()


def polish_notation(notation: str):
    """Решение польской нотации"""
    stack = Stack()
    operators = {'+': add, '-': sub, '*': mul, '/': floordiv}
    for i in notation:
        if i in operators:
            try:
                last_data = stack.pop()
                pre_last_data = stack.pop()
                result = operators[i](pre_last_data, last_data)
                stack.push(result)
            except EmptyStackError:
                return "Не корректный ввод данных"
        else:
            stack.push(int(i))
    return stack.pop()


def main():
    """Основная функция"""
    notation = input().split()
    print(polish_notation(notation))


if __name__ == '__main__':
    main()
