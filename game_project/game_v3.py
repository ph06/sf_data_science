"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def bsearch_predict(number: int=1, first: int=1, last: int=100) -> int:
    """Находим загаданное число методом бинарного поиска (рекурсивный способ)

    Args:
        number (int, optional): загаданное число. Defaults to 1.
        first (int, optional): начальный интервал поиска. Defaults to 1.
        last (int, optional): конечный интервал поиска. Defaults to 100.

    Returns:
        int: число попыток (количество вызовов рекурсивной функции)
    """
    mid = (first + last) // 2

    if mid == number:
        return 1
    elif mid > number:
        new_pos = mid - 1
        return 1 + bsearch_predict(number, first, new_pos)
    else:
        new_pos = mid + 1
        return 1 + bsearch_predict(number, new_pos, last)


def score_game(predict, debug=False) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        predict ([type]): функция угадывания
        debug (bool, optional): признак вывода отладочной информации. Defaults to False.

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    # Заполнили список количеством попыток поиска каждого загаданного числа
    for number in random_array:
        count_ls.append(predict(number))

    # Отладочный вывод количества попыток поиска для каждого числа
    if debug:
        for i, n in enumerate(count_ls):
            print(f'{random_array[i]}: {n} calls')
   
    score = int(np.mean(count_ls))  # посчитали среднее количество попыток поиска
    #print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")       
    return score


if __name__ == "__main__":
    # RUN
    #score_game(bsearch_predict, debug=True)
    print('Run benchmarking for game_core_v3: ', end='')
    print(score_game(bsearch_predict))