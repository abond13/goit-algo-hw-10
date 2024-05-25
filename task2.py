import matplotlib.pyplot as plt
import numpy as np
import random
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

def monte_carlo_integral(f, a, b, num_samples):
    # Генеруємо num_samples випадкових точок в інтервалі [a, b]
    samples = [random.uniform(a, b) for _ in range(num_samples)]
    
    # Обчислюємо середнє значення f(x) для випадкових точок
    avg_value = sum(f(x) for x in samples) / num_samples
    
    # Обчислюємо інтеграл за формулою середнього значення
    integral = (b - a) * avg_value
    
    return integral

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Обчислення інтеграла
result, error = spi.quad(f, a, b)

print("Інтеграл: ", result)

print("Інтеграл: ", monte_carlo_integral(f, a, b, 1000))
print("Інтеграл: ", monte_carlo_integral(f, a, b, 10000))
print("Інтеграл: ", monte_carlo_integral(f, a, b, 100000))