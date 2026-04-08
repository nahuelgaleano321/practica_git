import numpy as np
import matplotlib.pyplot as plt

# Pedir coeficientes al usuario
a = float(input("Ingresá el valor de a: "))
b = float(input("Ingresá el valor de b: "))
c = float(input("Ingresá el valor de c: "))

# Generar valores de x
x = np.linspace(-10, 10, 100)

# Función cuadrática
y = a * x**2 + b * x + c

# Graficar
plt.figure()
plt.plot(x, y)

# Detalles
plt.title(f"Grafico de f(x) = {a}x^2 + {b}x + {c}")
plt.xlabel("x")
plt.ylabel("f(x)")

plt.grid()

# Mostrar
plt.show()