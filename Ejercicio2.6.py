#Escribe una funcion invertir_palabras(texto) que reciba un string y devuelva el mismo string pero con las palabras en orden inverso.

#Ejemplo: Hola mundo Python -> Python mundo Hola

# Tu solución aquí
def invertir_palabras(texto):
    return  texto[::-1];

# Prueba
print(invertir_palabras("Hola mundo Python"))
print(invertir_palabras("IA es el futuro"))