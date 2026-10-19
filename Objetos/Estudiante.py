#Ejercicio 3.1
#Crea una clase Estudiante con los siguientes atributos:

#nombre
#edad
#notas (lista de numeros)
#promedio (calculado automaticamente en init)
#Y los siguientes metodos:

#agregar_nota(nota): anade una nota a la lista y recalcula el promedio
#info(): devuelve un string con el nombre, edad y promedio
#esta_aprobado(): devuelve True si el promedio >= 5.0
class Estudiante:
    def __init__(self,nombre,edad,notas):
        self.nombre = nombre;
        self.edad = edad;
        self.notas = notas;
        self.promedio = sum(self.notas) / len(notas);

    def agregar_nota(self,nota):
        self.notas.append(nota);
        self.promedio = sum(self.notas) / len(self.notas);

    def info(self):
        return f" {self.nombre} - {self.edad} - {self.promedio}";

    def esta_aprobado(self):
        return "Aprobado" if self.promedio >= 5 else "Suspenso";



barcola = Estudiante("Barcola",25,[1,2,3,4,5]);

print(barcola.esta_aprobado());


    



