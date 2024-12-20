import numpy as np
import matplotlib.pyplot as plt

reaction_times = np.random.normal(loc=500, scale=40, size=20)  # Среднее время = 500 мс

plt.figure(figsize=(8, 6))
plt.plot(reaction_times, 'o-', color='teal')
plt.axhline(reaction_times.mean(), color='red', linestyle='dashed', label=f'Среднее: {reaction_times.mean():.2f} мс')
plt.fill_between(range(20),
                 reaction_times.mean() - np.std(reaction_times),
                 reaction_times.mean() + np.std(reaction_times),
                 color='lightgreen', alpha=0.3, label=f'СКО: ±{np.std(reaction_times):.2f} мс')
plt.legend()
plt.title('Время реакции игрока')
plt.xlabel('Событие')
plt.ylabel('Время (мс)')
plt.show()