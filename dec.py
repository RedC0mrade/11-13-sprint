# 88836972
class QueueOverflowError(Exception):
    """Queue overflow."""


class EmptyListError(Exception):
    """Empty list error."""


class Deque:
    def __init__(self, number_limit: int):
        """Атрибуты очереди"""
        self.__gosh_queue = [None] * number_limit
        self.__max_number_limit = number_limit
        self.__head = -1
        self.__tail = 0
        self.__size = 0

    def push_back(self, value):
        """Добаавление значения в начало очереди"""
        if self.__size == self.__max_number_limit:
            raise QueueOverflowError
        self.__tail = self.__queue_count_function(self.__tail, -1)
        self.__gosh_queue[self.__tail] = value
        self.__size += 1

    def push_front(self, value):
        """Добаавление значения в начало очереди"""
        if self.__size == self.__max_number_limit:
            raise QueueOverflowError
        self.__head = self.__queue_count_function(self.__head, 1)
        self.__gosh_queue[self.__head] = value
        self.__size += 1

    def pop_front(self):
        """Получение и удаление значения первого значения очереди"""
        if self.__size == 0:
            raise EmptyListError
        data = self.__gosh_queue[self.__head]
        self.__gosh_queue[self.__head] = None
        self.__head = self.__queue_count_function(self.__head, -1)
        self.__size -= 1
        return data

    def pop_back(self):
        """Получение и удаление значения последнего значения очереди"""
        if self.__size == 0:
            raise EmptyListError
        data = self.__gosh_queue[self.__tail]
        self.__gosh_queue[self.__tail] = None
        self.__tail = self.__queue_count_function(self.__tail, 1)
        self.__size -= 1
        return data

    def __queue_count_function(self, item: int, num: int):
        """Вспомогательная переменная для подсчета места значения в очереди"""
        return (item + num) % self.__max_number_limit


def main():
    """Основная функция"""
    num = int(input())
    gosh_structure = Deque(int(input()))
    input_commands = [input().split() for _ in range(num)]
    for i in input_commands:
        try:
            if len(i) == 1:
                print(getattr(gosh_structure, i[0])())
            else:
                getattr(gosh_structure, i[0])(int(i[1]))
        except (EmptyListError, QueueOverflowError):
            print('error')


if __name__ == '__main__':
    main()
