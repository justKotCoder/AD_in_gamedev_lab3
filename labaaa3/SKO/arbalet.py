import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)  # Фиксируем рандом для воспроизводимости
shots = np.random.normal(loc=0, scale=5, size=(2, 2))  # Отклонения (x, y) из арбалета всего 2 выстрела

# Вычисляем отклонения (расстояния от центра цели)
distances = np.linalg.norm(shots, axis=1)

# Среднеквадратическое отклонение
std_dev = np.std(distances)

print(f"СКО отклонений: {std_dev:.2f} пикселей")

# Визуализация попаданий
plt.figure(figsize=(6, 6))
plt.scatter(shots[:, 0], shots[:, 1], color='red', label='Попадания')
plt.scatter(0, 0, color='blue', label='Цель', s=100)
plt.xlim(-20, 20)
plt.ylim(-20, 20)
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.legend()
plt.title("Модель разброса выстрелов")
plt.gca().set_aspect('equal', adjustable='box')
plt.show()


