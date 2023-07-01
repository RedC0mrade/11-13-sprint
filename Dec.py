# 88701821
class GoshsDek:
    def __init__(self, number_limit: int):
        self.gosh_desc = [None] * number_limit
        self.max_number_limit = number_limit
        self.first_elem = -1
        self.last_elem = 0
        self.size = 0

    def push_back(self, value):
        if self.size != self.max_number_limit:
            self.last_elem = (self.last_elem - 1) % self.max_number_limit
            self.gosh_desc[self.last_elem] = value
            self.size += 1
        else:
            print('error')

    def push_front(self, value):
        if self.size != self.max_number_limit:
            self.first_elem = (self.first_elem + 1) % self.max_number_limit
            self.gosh_desc[self.first_elem] = value
            self.size += 1
        else:
            print('error')

    def pop_front(self):
        if self.size == 0:
            print('error')
        else:
            data = self.gosh_desc[self.first_elem]
            self.gosh_desc[self.first_elem] = None
            self.first_elem = (self.first_elem - 1) % self.max_number_limit
            self.size -= 1
            print(data)

    def pop_back(self):
        if self.size == 0:
            print('error')
        else:
            data = self.gosh_desc[self.last_elem]
            self.gosh_desc[self.last_elem] = None
            self.last_elem = (self.last_elem + 1) % self.max_number_limit
            self.size -= 1
            print(data)


if __name__ == '__main__':
    num = int(input())
    gosh_structure = GoshsDek(int(input()))
    functions = {'push_back': gosh_structure.push_back,
                 'push_front': gosh_structure.push_front,
                 'pop_front': gosh_structure.pop_front,
                 'pop_back': gosh_structure.pop_back}
    input_commands = [input().split() for _ in range(num)]
    # for i in input_commands:
    #     if len(i) == 1:
    #         functions[i[0]]()
    #     else:
    #         functions[i[0]](int(i[1]))
    [functions[i[0]]() if len(i) == 1 else
     functions[i[0]](int(i[1])) for i in input_commands]
