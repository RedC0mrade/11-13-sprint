from operator import add, floordiv, mul, sub

operators = {'+': add, '-': sub, '*': mul, '/': floordiv}


class Stack:

    def __init__(self):
        self.dek = []
        self.head = 0
        self.operations = []

    def polish_notation(self, notation: str):

        list(filter(lambda x: self.dek.append(int(x)) if x.isdigit() or (
                x.startswith('-') and x[1:].isdigit()) else
                self.operations.append(x), notation.split()))
        self.head = len(self.dec) - 1
        for operation in self.operations:
            if self.head > 1:
                self.dek[self.head - 1] = operators[operation](
                    self.dek[self.head - 1], self.dek[self.head])
                self.head -= 1
            else:
                return self.dek[self.head]
        return self.dek[0]


calculator = Stack()
print(calculator.polish_notation(input()))
