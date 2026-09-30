#Ejercicio 2.5
#Dado un texto, escribe un programa que cuente cuantas veces aparece cada palabra (sin distincion de mayúsculas/minúsculas). Devuelve un diccionario con las frecuencias.

#Ejemplo: Hola hola Hola -> hola: 3

# Tu solución aquí
texto = "Hola hola Hola Python python PYTHON"

frecuencias = {}

# Escribe tu código aquí

for palabra in texto.split():
    palabra = palabra.casefold()

    if palabra in frecuencias:
        frecuencias[palabra] += 1
    else:
        frecuencias[palabra] = 1
    print(frecuencias);


# Muestra el resultado
print(frecuencias)
