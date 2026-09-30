#Ejercicio 2.4
#Crea una lista con los primeros 20 números de Fibonacci. Los dos primeros son 1, cada siguiente número es la suma de los dos anteriores.

#Usa un bucle for y el método .append().


# Tu solucion aqui
# Genera la secuencia de Fibonacci con los primeros 20 numeros
fibonacci = []

# Tu código aquí

a = 0;
b = 1;
c = 0;

for i in range(1,21):

    fibonacci.append(a);

    c = a + b;
    a = b;
    b = c;

print(f"Primeros 20 números de Fibonacci: {fibonacci}")