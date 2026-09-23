#### Ejercicio 2.2

#Escribe una expresion ternaria que devuelva par o impar segun un
#numero entero. Prueba con varios valores.
# Tu solucion aqui
numeros = [4, 7, 12, -3, 0]

for n in numeros:
    resultado = "Par" if n%2==0 else "Impar"
    print(f"{n} -> {resultado}");