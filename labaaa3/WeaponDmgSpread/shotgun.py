import numpy as np
import matplotlib.pyplot as plt

# Генерация случайных значений урона с нормальным распределением
np.random.seed(123)
damage = np.random.normal(loc=66.67, scale=4.52, size=100)

# Визуализация гистограммы урона
plt.figure(figsize=(8, 6))
plt.hist(damage, bins=10, color='purple', alpha=0.7, edgecolor='black')
plt.axvline(damage.mean(), color='red', linestyle='dashed', linewidth=2, label=f'Среднее: {damage.mean():.2f}')
plt.axvline(damage.mean() + np.std(damage), color='green', linestyle='dotted', label=f'СКО: {np.std(damage):.2f}')
plt.axvline(damage.mean() - np.std(damage), color='green', linestyle='dotted')
plt.legend()
plt.title('Распределение урона оружия')
plt.xlabel('Урон')
plt.ylabel('Частота')
plt.show()