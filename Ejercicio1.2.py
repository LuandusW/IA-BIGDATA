#### Ejercicio 1.2 — Conversor de temperatura
#Crea un programa que pida una temperatura en grados Celsius y la convierta a Fahrenheit usando la fórmula: `F = (C × 9/5) + 32`.

tempC = int(input("Introduce una temperatura"));

formula = (tempC * (9/5) + 32);

print(f"La temperatura en Fahrenheit es: {formula}");