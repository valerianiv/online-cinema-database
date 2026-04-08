import numpy as np
import matplotlib.pyplot as plt

# Исходные точки
X = np.array([[-1, 0], [-2, 0], [0, 0]])
y = np.array([1, -1, -1])  # Метки классов

# Функция для вычисления f(x)
def f(x1, x2):
    return 6*(1 + x1)**2 - 2*(1 + 2*x1)**2 - 5

# Создание сетки для графика
x1_grid = np.linspace(-3, 1, 100)
x2_grid = np.linspace(-1, 1, 100)
X1, X2 = np.meshgrid(x1_grid, x2_grid)
Z = f(X1, X2)

# Построение графика
plt.figure(figsize=(8, 6))
plt.scatter(X[y == 1, 0], X[y == 1, 1], color='blue', label='Класс ω₁ (x₁)', s=100)
plt.scatter(X[y == -1, 0], X[y == -1, 1], color='red', label='Класс ω₂ (x₂, x₃)', s=100)
plt.contour(X1, X2, Z, levels=[0], colors='black', linestyles='dashed')
plt.fill_between(x1_grid, -1, 1, where=(f(x1_grid, 0) >= 0, color='blue', alpha=0.1)
plt.fill_between(x1_grid, -1, 1, where=(f(x1_grid, 0) < 0), color='red', alpha=0.1)
plt.xlabel('Ось x₁')
plt.ylabel('Ось x₂')
plt.title('SVM с полиномиальным ядром (K(x,y) = (1 + xᵀy)²)')
plt.legend()
plt.grid(True)
plt.show()