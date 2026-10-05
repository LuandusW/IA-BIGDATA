import csv

# Tu solución aquí

# Paso 1: Crear el archivo CSV con datos de alumnos
datos_alumnos = [
    ["Nombre", "Edad", "Nota"],
    ["Ana", 22, 8.5],
    ["Carlos", 24, 9.2],
    ["Beatriz", 21, 7.8],
    ["David", 23, 6.5],
    ["Elena", 22, 9.8],
]

# Escribe tu código aquí
#with open("datos.csv", "w", encoding="utf-8",newline="") as archivo:
#    escritor = csv.writer(archivo, delimiter=",");
#    for alumno in datos_alumnos:
#        escritor.writerow(alumno);
#print("Archivo creado.");

# Paso 2: Leer el CSV y calcular la nota media
# Escribe tu código aquí
sumaTotal = 0;
alumnos = 0;
with open("datos.csv", "r", encoding="utf-8") as archivo:
    lector = csv.reader(archivo);
    for fila in lector:
        if fila[2] == "Nota" :
            continue;
        sumaTotal+=float(fila[2]);
        alumnos+=1;

print(f"La media es: {sumaTotal / alumnos}");


# Paso 3: Encontrar el alumno con mayor nota
# Escribe tu código aquí

nota = 0;
alumnoMayorNota = "";
with open("datos.csv","r",encoding="utf-8") as archivo:
    lector = csv.reader(archivo);
    for fila in lector:
        if fila[2] == "Nota":
            continue;
        if float(fila[2]) > nota:
            nota = float(fila[2]);
            alumnoMayorNota = fila;


print(f"El alumno con la mayor nota: {nota} es: {alumnoMayorNota} ");
  