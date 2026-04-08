import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-2, 2, 100)

y = np.exp(x)


plt.figure()
plt.plot(x, y)


plt.title("Grafico de f(x) = e^x")
plt.xlabel("x")
plt.ylabel("f(x)")

plt.grid()


plt.show()