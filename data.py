import pandas as pd

data = {
    "Fecha": ["2024-01-01", "2024-01-01", "2024-01-02", "2024-01-02", "2024-01-03", "2024-01-03"],
    "Provincia": ["Buenos Aires", "Cordoba", "Buenos Aires", "Cordoba", "Buenos Aires", "Cordoba"],
    "Tests": [100, 80, 120, 90, 110, 95],
    "Positivos": [20, 10, 25, 15, 22, 14]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

print("\nTotal de tests por provincia:")
print(df.groupby("Provincia")["Tests"].sum())

print("\nTotal de positivos por provincia:")
print(df.groupby("Provincia")["Positivos"].sum())

print("\nPromedio de positivos por provincia:")
print(df.groupby("Provincia")["Positivos"].mean())

print("\nProvincia con más positivos:")
print(df.groupby("Provincia")["Positivos"].sum().idxmax())

df["Porcentaje_Positividad"] = (df["Positivos"] / df["Tests"]) * 100

print("\nDataFrame con porcentaje de positividad:")
print(df)

print("\nPromedio de porcentaje de positividad por provincia:")
print(df.groupby("Provincia")["Porcentaje_Positividad"].mean())