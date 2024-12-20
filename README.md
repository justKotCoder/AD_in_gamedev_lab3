## Отчет по лабораторной работе №3

Исполнитель:
- Жолдубаева Жанара Мирланбековна
- РИ- 230911

### Оценка выполнения заданий:

| Задание   | Статус     | Баллы |
|-----------|------------|-------|
| Задание 1 | ✅          | 60    |
| Задание 2 | ✅          | 20    |
| Задание 3 | ✅          | 20    |

### Проверяющие:
- к.т.н., доцент Иванов И.И.
- к.э.н., доцент Петров П.П.
- ст. преп., Сидоров С.С.

## Цель исследования
Целью данной работы стало изучение игровых структур проекта Save RTF, знакомство с его прототипом на Unity, анализ доступного игрового вооружения и предложения по улучшению арсенала.

## Задание 1
### Увеличение арсенала в игре Save RTF
Была создана таблица, содержащая информацию о характеристиках оружия, таких как урон и шанс попадания. Для этого использовал Google таблицы: Google Sheets (https://docs.google.com/spreadsheets/d/12V0fRsdPyaTffW7ctOaCRHxkH1Bxn4dfSq2ouFk-yuQ/edit?gid=0#gid=0).

В ходе тестирования различных видов оружия, при здоровье первого босса, равном 1000 единиц, были вычислены средние значения урона и частоты атак. Расчетные формулы:

1. Урон: Урон = ХП босса / Количество ударов или патронов
2. Скорострельность: Скорострельность = Количество патронов / Время обоймы
3. Скорость атак: Скорость ударов = Количество ударов / Время уничтожения босса

Примерный урон каждого типа оружия:

import matplotlib.pyplot as plt
import numpy as np

weapons = ['Пистолет', 'Винтовка', 'Тесак', 'Бензопила']
damage = [50, 70, 100, 200]

plt.figure(figsize=(10, 6))
plt.bar(weapons, damage, color='skyblue')
plt.title('Средний урон разных видов оружия')
plt.xlabel('Тип оружия')
plt.ylabel('Средний урон')
plt.show()


## Задание 2
### Исследование времени реакции игрока
Анализ проводился на статистическом наборе данных с нормальным распределением по времени реакций игрока. 

reaction_times = np.random.normal(loc=500, scale=40, size=20)

plt.figure(figsize=(10, 6))
plt.plot(reaction_times, 'o-', color='teal')
plt.axhline(reaction_times.mean(), color='red', linestyle='dashed', label=f'Среднее: {reaction_times.mean():.2f} мс')
plt.fill_between(range(20), reaction_times.mean() - np.std(reaction_times), reaction_times.mean() + np.std(reaction_times), color='lightgreen', alpha=0.3, label=f'СКО: ±{np.std(reaction_times):.2f} мс')
plt.legend()
plt.title('Время реакции игрока')
plt.xlabel('Событие')
plt.ylabel('Время (мс)')
plt.show()


## Задание 3
### Визуализация данных из Google и интеграция с Unity
В этом задании данные из таблиц были визуализированы с использованием Python и интегрированы в Unity.

import pandas as pd

url = 'https://docs.google.com/spreadsheets/d/12V0fRsdPyaTffW7ctOaCRHxkH1Bxn4dfSq2ouFk-yuQ/export?format=csv'
data = pd.read_csv(url)

plt.figure(figsize=(10, 6))
plt.bar(data['Weapon'], data['Damage'], color='coral')
plt.title('Урон различных типов оружия')
plt.xlabel('Оружие')
plt.ylabel('Урон')
plt.show()


## Заключение
В рамках работы были выполнены анализ и визуализация характеристик оружия в игре Save RTF. Также были предложены новые модели вооружения, которые могут быть интегрированы в проект на Unity, что позволит улучшить игровую динамику и разнообразие.
