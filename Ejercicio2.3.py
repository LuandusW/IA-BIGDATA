#Escribe un programa que imprima la tabla de multiplicar del numero que pase el usuario (del 1 al 10). Usa un bucle for con range().

# Tu solucion aqui
numero = int(input("Introduce un numero 1 - 10"));  # Puedes cambiar este valor

if numero <= 10 and numero > 0:
    for i in range(10):
        print(f"{i+1} * {numero} = {(i +1) * numero}");
else:
    print("El numero tiene que estar en el rango 1-10");

# Escribe tu bucle aquí