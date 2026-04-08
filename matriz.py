import numpy as np

# Crear matriz 3x3 ingresada por el usuario
print("Ingresá los valores de la matriz 3x3:")

matriz = []

for i in range(3):
    fila = []
    for j in range(3):
        valor = float(input(f"Elemento [{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)

# Convertir a array de numpy
A = np.array(matriz)

# Mostrar matriz original
print("\nMatriz A:")
print(A)

# Traspuesta
AT = A.T
print("\nTraspuesta de A:")
print(AT)

# Producto punto (dot)
producto = np.dot(A, AT)
print("\nProducto A · A^T:")
print(producto)