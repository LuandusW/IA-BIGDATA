#***
#### Ejercicio 2.1

#Escribe una funcion `clasificar_edad(edad)` que devuelva:
#- Bebe si `edad < 2`
#- Niño si `2 <= edad < 13`
#- Adolescente si `13 <= edad < 18`
#- Adulto si `18 <= edad < 65`
#- Adulto mayor si `edad >= 65`

# Tu solucion aqui
def clasificar_edad(edad):
     match (edad):
          case edad if edad < 2:
               return "Bebe";
          case edad if edad >= 2 and edad <= 13:
               return "Niño";
          case edad if edad >= 13 and edad < 18:
               return "Adolescente";
          case edad if edad >= 18 and edad < 65:
               return "Adulto";
          case edad if edad >= 65:
               return "Adulto mayor";

for edad in [1, 5, 15, 25, 70]:
    print(f"{edad} años -> {clasificar_edad(edad)}")