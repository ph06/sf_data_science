# Проект 0. Угадай число

## Оглавление  
[1. Описание проекта](#Описание-проекта)  
[2. Какой кейс решаем?](#Какой-кейс-решаем)  
[3. Краткая информация о данных](#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](#Этапы-работы-над-проектом)  
[5. Результат](#Результат)    
[6. Выводы](#Выводы) 

### Описание проекта    
Угадать загаданное компьютером число за минимальное число попыток.

:arrow_up:[к оглавлению](#Оглавление)


### Какой кейс решаем?    
Нужно написать программу, которая угадывает число за минимальное число попыток

**Условия соревнования:**  
- Компьютер загадывает целое число от 1 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число»;
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**     
Результаты оцениваются по среднему количеству попыток при 1000 повторений

**Что практикуем**     
Учимся писать хороший код на python


### Краткая информация о данных
В качестве исходных данных программа генерирует 1000 случайных целых чисел в интервале от 1 до 100.

Данная [ссылка](https://github.com/SkillfactoryDS/RecomendationSystemOfBooks/blob/master/data/ratings.csv) - проверка механизма работы файла исключений .gitignore.
Файл по ссылке (~70 Mb csv-файл) находится в папке с текущим проектом и в репозитарий попасть не должен, поскольку расширение csv добавлено в список игнорируемых для репликации файлов.
  
:arrow_up:[к оглавлению](#Оглавление)


### Этапы работы над проектом  
- Реализация рекурсивного алгоритма бинарного поиска в среде IDE VS Code;
- Отладка алгоритма поиска на тестовых значениях;
- Приведение исходного кода к возможности вызова как отдельного модуля, так и автономного запуска;
- Адаптация шаблона Jupyter Notebook для вызова функций из внешнего модуля.

:arrow_up:[к оглавлению](#Оглавление)


### Результаты:  
Полученные результаты полностью соответствуют требованиям: в среднем, число находится за 5 попыток поиска из допустимых 20.

:arrow_up:[к оглавлению](#Оглавление)


### Выводы:  
Выбор и алгоритма бинарного поиска для нахождения искомого числа обоснован и показал эффективные результаты, которые в 4 раза превосходят допустимую норму.

:arrow_up:[к оглавлению](#Оглавление)


Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами