#### Ejercicio 1.3 — Intercambio de variables
##Dadas dos variables `a = 10` y `b = 20`, intercambia sus valores sin usar una tercera variable.

a = 10;
b = 20;
print(f"A vale {a} y B vale {b}");
a,b = b,a
print(f"Tras cambiar A vale: {a} y B vale {b}");