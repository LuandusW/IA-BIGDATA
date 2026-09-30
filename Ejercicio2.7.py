#Ejercicio 2.7¶
#Escribe una funcion filtrar_y_transformar(lista, criterio) que reciba:

#lista: una lista de números
#criterio: una funcion lambda (por ejemplo lambda x: x > 5)
#La funcion debe devolver una nueva lista con los números que cumplen el criterio, multiplicados por 2.

#Ejemplo: filtrar_y_transformar([1, 3, 7, 10], lambda x: x > 5) -> [14, 20]

# Tu solución aquí
def filtrar_y_transformar(lista, criterio):
    # Escribe tu código aquí
    return [x * 2 for x in lista if criterio(x)];

# Prueba
lista = [1, 3, 7, 10, 2, 15];
resultado = filtrar_y_transformar(lista, lambda x: x > 5)
print(f"Resultado: {resultado}")  # [14, 20, 30]