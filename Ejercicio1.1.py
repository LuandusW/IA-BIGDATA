### 3.6. Ejercicios propuestos

#### Ejercicio 1.1 — Calculadora de descuentos
#Crea un programa que pida al usuario el precio original de un artículo y el porcentaje de descuento aplicado. El programa debe calcular y mostrar el precio final después del descuento.

#Además, el programa debe clasificar el descuento en una de estas categorías:

#- Sin descuento: 0 %
#- Oferta: entre 1 % y 15 %
#- Gran oferta: entre 16 % y 40 %
#- Liquidación: más del 40 %

#```python
# Pista: usa float() para convertir los inputs
# precio_final = precio_original * (1 - descuento / 100)
#```

precio = int(input("Introduce el precio del producto"));
descuento = int(input("Introduce el descuento"));

match(descuento):
    case descuento if descuento == 0:
        print(f"El precio del producto es: {precio} - Sin descuento");
    case descuento if descuento > 0 and descuento < 16:
        print(f"El precio del producto es: {precio  - ((precio * descuento) / 100)} - Oferta" );
    case descuento if descuento >= 16 and descuento <= 40:
        print(f"El precio del producto es: {precio  - ((precio * descuento) / 100)} -  Gran Oferta");
    case descuento if descuento > 40:
        print(f'El precio del producto es: {precio  - ((precio * descuento) / 100)} - Liquidación');
        

