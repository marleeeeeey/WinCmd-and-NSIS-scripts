﻿# %matplotlib inline
from IPython import get_ipython
get_ipython().magic('matplotlib inline')

import operator

import numpy as np
from numpy.random import randn

import matplotlib.pyplot as plt

from pandas import Series, DataFrame
import pandas as pd


import imp
import my_module
imp.reload(my_module)   # перезагрузка модуля в любом случае


# # автоматический вызов отладчика при возникновении исключения
# %pdb


# **************************************************************************
# *********************** S K L E A R N ************************************
# **************************************************************************

import sklearn
import sklearn.svm as svm
import sklearn.grid_search as grid_search




# **************************** МОДЕЛИ / МЕТОДЫ *****************************

# sklearn.linear_model - реализация линейных методов
# Perceptron - реализация метода Перцептрона
#    fit     - обучение
#    predict - построение прогнозов
from sklearn.linear_model import Perceptron


# Реализация метода опорных векторов (Support Vector Machine, SVM) 
#    C          - коэфициент
#    kernel     - тип ядра (линейное ядро — kernel='linear')
#    support_   - индексы опорных объектов
#    coef_      - веса каждого признака у обученного классификатора
#    get_feature_names() - понять какому слову соотвествует i признак
from sklearn.svm import SVC


# Решение задачи КЛАССИФИКАЦИИ с помощью метода k ближайших соседей
from sklearn.neighbors import KNeighborsClassifier


# Решение задачи РЕГРЕССИИ с помощью метода k ближайших соседей
#    metric - название метрики
#    weights='distance' — данный параметр добавляет в алгоритм веса, 
#                         зависящие от расстояния до ближайших соседей.
from sklearn.neighbors import KNeighborsRegressor







# ***************************** МЕТРИКИ ************************************

# В качестве метрики качества мы будем 
# использовать долю верных ответов (accuracy)
# первым аргументом которой является вектор правильных ответов, 
# а вторым — вектор ответов алгоритма
from sklearn.metrics import accuracy_score


# Реализация метрики AUC. 
#    y_true     - вектор истинных ответов, 
#    y_score    - вектор с оценками принадлежности объектов к первому классу.
# AUC-ROC (Area Under ROC-Curve) предназначена для алгоритмов бинарной 
# классификации, выдающих оценку принадлежности объекта к одному из классов. 
# По сути, значение этой метрики является агрегацией показателей качества 
# всех алгоритмов, которые можно получить, выбирая какой-либо порог для 
# оценки принадлежности.
from sklearn.metrics import roc_auc_score







# ********************* МАСШТАБАТОРЫ / ПРЕДОБРАБОТЧИКИ *********************

# Приведение признаков к одному масштабу 
# на вход необходимо подать матрицу признаков и 
# получить масштабированную матрицу, в которой 
# каждый столбец имеет нулевое среднее значение и 
# единичное стандартное отклонение
from sklearn.preprocessing import scale


# StandardScaler - класс используется для стандартизации признаков
#    fit_transform 
#        находит параметры нормализации 
#        (средние и дисперсии каждого признака) 
#        по выборке, и сразу же делает нормализацию выборки 
#        с использованием этих параметров. 
#    transform 
#       делает нормализацию на основе уже найденных параметров.
from sklearn.preprocessing import StandardScaler








# *********************** ГЕНЕРАТОРЫ РАЗБИЕНИЙ ****************************


# генератор разбиений 
# который задает набор разбиений на обучение и валидацию
from sklearn.cross_validation import KFold


# Вычисляет качество на всех разбиениях
# Возвращает массив(результы по каждому разбиению), 
# который нужно усрединить
#    estimator - передается классификатор, 
#    cv - генератор разбиений с предыдущего шага. 
#    scoring='mean_squared_error' - использовать в качестве
#       метрики среднеквадратичную ошибку
from sklearn.cross_validation import cross_val_score







# ************************** ТЕКСТОВЫЕ ПРОЦЕССОРЫ *************************


# Для построения числового представления из текстовых данных
# применяется вычисление TF-IDF
# Это показатель, который равен произведению двух чисел: 
# TF (term frequency) и IDF (inverse document frequency). 
# Первая равна отношению числа вхождений слова в документ к общей длине документа. 
# Вторая величина зависит от того, в скольки документах выборки встречается это слово. 
# Чем больше таких документов, тем меньше IDF. Таким образом, TF-IDF будет иметь 
# высокое значение для тех слов, которые много раз встречаются в данном документе, 
# и редко встречаются в остальных.
#   fit_transform - преобразование обучающей выборки 
#   transform - для преобразования тестовой выборки
from sklearn.feature_extraction.text import TfidfVectorizer







# *************************** ИСТОЧНИКИ ДАННЫХ ****************************


# Для данных датасетов, доступных в scikit-learn'е
# Готовые выборки, предназначенные для тестов
#
# newsgroups = datasets.fetch_20newsgroups(subset='all', 
#                     categories=['alt.atheism', 'sci.space'])
#   newsgroups.data - массив с текстами
#   newsgroups.target - номер класса
from sklearn import datasets







# ********************* РЕАЛИЗАЦИЯ РЕШАЮЩИХ ДЕРЕВЬЕВ *********************
# sklearn.tree.DecisionTreeСlassifier - для классификации
# sklearn.tree.DecisionTreeRegressor - для регрессии
#   fit() - обучение модели
#   predict() - построение прогнозов
#   importances - переменная, которая содержит массив "важностей" признаков
# ************************************************************************




# **************************************************************************
# **************************************************************************
# **************************************************************************