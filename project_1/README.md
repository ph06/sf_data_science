<center><img src=https://raw.githubusercontent.com/AndreyRysistov/DatasetsForPandas/main/hh%20label.jpg alt="drawing" width="400"/></center>

# Проект 1. Анализ резюме из HeadHunter

## Оглавление  
1. [Описание проекта](#Описание-проекта)
2. [Описание данных](#Описание-данных)
3. [Зависимости](#Зависимости)
4. [Установка](#Установка-проекта)
5. [Использование](#Использование)
6. [Авторы](#Авторы)
7. [Выводы](#Выводы)

## Описание проекта
В нашем распоряжении будет база резюме, выгруженная с сайта поиска вакансий [HeadHunter](https://hh.ru).

*Проблематика: часть соискателей не указывает желаемую заработную плату, когда составляет своё резюме.*

Чем это плохо?
Это является помехой для рекомендательной системы HeadHunter, которая подбирает соискателям список наиболее подходящих вакансий, а работодателям — список наиболее подходящих специалистов.

>⭐ Компания HeadHunter хочет построить модель, которая бы автоматически определяла примерный уровень заработной платы, подходящей пользователю, исходя из информации, которую он указал о себе. Но, как вы знаете, прежде чем построить модель, данные необходимо преобразовать, исследовать и очистить. В этом и состоит наша с вами задача!

**ОРГАНИЗАЦИОННАЯ ИНФОРМАЦИЯ**

Наш проект будет состоять из четырёх частей:

* базовый анализ структуры данных
* преобразование данных
* разведывательный анализ
* очистка данных

**Данный проект** направлен на демонстрацию применения различных методов преобразования, разведывательного анализа и очистки данных на каждом из её этапов на примере датасета базы резюме, выгруженной с сайта поиска вакансий hh.ru.

**О структуре проекта:**
* [data](./data) - папка с исходными табличными данными (база резюме и курсы валют). База резюме предварительно разбита на chunks
* [Project-1.ipynb](./Project-1.ipynb) - jupyter-ноутбук, содержащий код проекта, в котором демонстрируются методы и подходы решения задач преобразования, разведывательного анализа и очистки данных. **ВНИМАНИЕ!** Для корректного отображения интерактивных графиков Plotly в онлайне, необходимо использовать специальный сервис [nbviewer](https://nbviewer.org/github/ph06/sf_data_science/blob/main/project_1/Project-1.ipynb)
* [requirements.txt](./requirements.txt) и [.python-version](./.python-version) - вспомогательные файлы для воспроизводимости среды выполнения


## Описание данных
В этом проекте используются данные базы резюме, выгруженной с сайта поиска вакансий [HeadHunter](https://hh.ru), а также данные с курсами валют за период с 29.12.2017 по 05.12.2019 г.

>Данные базы резюме были предварительно преобразованы из представленного CSV-файла размером 455.5 MБ для возможности размещения на платформе [GitHub](https://github.com):
>* разделены на 5 чанков с максимальным размером 10 тыс. строк каждый. Код разделения представлен в исходном коде проекта
>* сохранены в CSV-формате (с разделителем по-умолчанию) с запаковыванием данных для минимизации занимаемого размера в репозитории

Исходный датасет базы резюме представляет собой набор данных в "сыром" виде из таблицы с 44744 строками и 12 признаками. Курсы валют представлены таблицей, состоящей из 5664 строк и 7 признаков за период с 29.12.2017 по 05.12.2019 г.


## Зависимости
* Python (3.12.2 - использовался менеджер версий pyenv):
    * [numpy (1.26.4)](https://numpy.org)
    * [pandas (2.2.2)](https://pandas.pydata.org)
    * [Plotly (5.22.0)](https://plotly.com/python/)
    * [Plotly Express (5.22.0)](https://plotly.com/python/plotly-express/)


## Установка проекта
```
git clone https://github.com/ph06/sf_data_science/tree/main/project_1
pyenv install 3.12.2
pip install -r requirements.txt
```

## Использование
Вся информация о работе представлена в jupyter-ноутбуке [Project-1.ipynb](./Project-1.ipynb).

**ВНИМАНИЕ!**
Для корректного отображения интерактивных графиков Plotly в онлайне, необходимо использовать специальный сервис [nbviewer](https://nbviewer.org/github/ph06/sf_data_science/blob/main/project_1/Project-1.ipynb)

## Авторы
* [Phobius](https://github.com/ph06/)


## Выводы
В результате выполнения данного проекта были отработаны базовые навыки применения различных методов преобразования, разведывательного анализа и очистки данных на каждом из последовательных этапов. Дополнительно были отработаны конструкции Python: разделение и склеивание DataFrame через chunks (обход ограничений GutHub для хранения в репозитории объемных таблиц), использование lambda-функций, List Comprehension, тернарного и "моржового" операторов и пр. (т.н. "синтаксический сахар") для сокращения и упрощения кода. При написании jupyter-ноутбука были использованы рекомендации соглашения **PEP 8** по оформлению исходного кода и комментариев. Опробованы различные методы отображения интерактивных графиков на базе библиотек Plotly и Plotly Express, а также сторонней платформы по визуализации jupyter-ноутбуков с использованием данных библиотек - [nbviewer](https://nbviewer.org/github/ph06/sf_data_science/blob/main/project_1/Project-1.ipynb).