"""### Ejercicio 2.8
 
Escribe una funcion procesar_lista(lista) que reciba una lista de
elementos y:
1. Sumar todos los números (ignora los que no sean numéricos)
2. Si hay un valor negativo, lanzar una ValueError
3. Si la lista está vacía, lanzar un ValueError
4. Devolver la suma total
 
Prueba con diferentes listas."""

def procesar_lista(lista):
    if not lista:
        raise ValueError("La lista está vacía")

    suma = 0

    for elemento in lista:
        if isinstance(elemento, (int, float)):
            if elemento < 0:
                raise ValueError("La lista contiene un valor negativo")
            suma += elemento

    return suma

print(procesar_lista([1, 2, 3, 4]))         
print(procesar_lista([1, "hola", 2, "x"]))   
print(procesar_lista([1.5, 2, 3.5]))        

try:
    print(procesar_lista([1, -2, 3]))
except ValueError as e:
    print(e)

try:
    print(procesar_lista([]))
except ValueError as e:
    print(e)