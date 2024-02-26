# 89063266

class Participant:
    """Класс участников"""
    def __init__(self, login: str, solution: int, fine: int) -> None:
        """Инициализация объектов класс"""
        self._login = login
        self._solution = solution
        self._fine = fine

    def __lt__(self, other: "Participant") -> bool:
        """Сравнение участников"""
        return ((other._solution, self._fine, self._login)
                < (self._solution, other._fine, other._login))

    def __str__(self):
        """Вывод логина"""
        return self._login


def separation(results: list, left: int, right: int) -> int:
    """Функция разделения списка"""
    centr = results[left]
    next_left = left + 1
    while True:
        while next_left <= right and results[next_left] < centr:
            next_left += 1
        while next_left <= right and results[right] > centr:
            right -= 1
        if next_left >= right:
            break
        results[next_left], results[right] = results[right], results[next_left]
        next_left += 1
        right -= 1
    results[left], results[right] = results[right], results[left]
    return right


def sorting(results: list, left=0, right=None) -> None:
    """Функция сортировки"""
    if right is None:
        right = len(results) - 1
    if left >= right:
        return
    centr = separation(results, left, right)
    sorting(results, left, centr - 1)
    sorting(results, centr + 1, right)


def main() -> None:
    """Основная функция"""
    participants = int(input())
    results = [
        Participant(line[0], int(line[1]), int(line[2]))
        for line in (input().split() for _ in range(participants))]
    sorting(results)
    print(*results, sep='\n')


if __name__ == '__main__':
    main()
