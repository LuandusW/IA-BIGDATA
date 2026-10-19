#### Ejercicio 3.3


"""
__Clase `Tienda` con métodos mágicos__

Crea una clase `Tienda` que gestione un catálogo de productos y demuestre el uso de **múltiples métodos mágicos**.

__Requisitos__

__Clase `Producto`__
Cada producto tiene:
- `nombre` (str)
- `precio` (float)
- `stock` (int)

Y debe implementar:
- `__init__(nombre, precio, stock)`
- `__str__()` → `"Nombre: Precio€ (Stock: N)"`
- `__repr__()` → `Producto('Nombre', 9.99, 5)`
- `__bool__()` → `False` si `stock == 0`, `True` en otro caso
- `__mul__(self, cantidad)` → devuelve un `float` (precio × cantidad)

__Clase `Tienda`__
Gestiona una lista de productos. Debe implementar:

| Método mágico | Propósito | Operación |
|---------------|-----------|-----------|
| `__init__(nombre)` | Inicializar tienda con nombre vacío | `tienda = Tienda("MiTienda")` |
| `__len__()` | Devolver número de productos | `len(tienda)` |
| `__getitem__(index)` | Acceder a un producto por índice | `tienda[0]` |
| `__iter__()` | Recorrer productos con `for` | `for p in tienda:` |
| `__contains__(nombre)` | Buscar producto por nombre | `"Laptop" in tienda` |
| `__str__()` | Representación legible | `print(tienda)` |
| `__repr__()` | Representación oficial | `repr(tienda)` |
| `__bool__()` | `False` si tienda vacía | `if tienda:` |
| `__eq__(otra)` | Comparar dos tiendas por número de productos | `tienda1 == tienda2` |
| `__format__(fmt)` | Formateo personalizado | `f"{tienda:inventario}"` |
| `__add__(otra)` | Combinar dos tiendas | `tienda1 + tienda2` |
| `__enter__()` / `__exit__()` | Context manager | `with Tienda("X") as t:` |
"""


class Tienda:

    def __init__(self,nombre):
        self.nombre = nombre;
        self._productos = [];

    def __len__(self):
         return len(self._productos);
    def __getitem__(self,index):
         return self._productos[index];
    def __iter__(self):
         for p in self._productos:
              print(f"Productos:  {p}");
    def __contains__(self,nombre):
         return any(p.nombre == nombre for p in self._productos);
    def __str__(self):
         return print(f"Tienda: {self._productos}");
    def __repr__(self):
         return repr(self._productos);

    def __bool__(self):
        if len(self._productos) < 1:
            return False;
        else: 
            return True;

    def __eq__(self, otra):
        if not isinstance(otra, Tienda):
            return NotImplemented

        return len(self) == len(otra)

    def __format__(self, fmt):
        if fmt == "resumen":
            productos = ", ".join(p.nombre for p in self._productos)
            return f"({self.nombre} inventario: {productos})"

        return str(self)

    def __add__(self,otra):
         self._productos.append(otra);

    def __enter__(self):
        print(f">>> Abriendo tienda {self.nombre}");
        return  self;
    def __exit__(self):
        print(f">>> Cerrando tienda {self.nombre}");
        return self;

    def buscar(self,nombre):
         return nombre()


         


class Producto:

    def __init__(self,nombre,precio,stock):
        self.nombre = nombre;
        self.precio = precio;
        self.stock = stock;

    def __str__(self):
        print (f"Nombre: {self.nombre} Precio: {self.precio} Stock: {self.stock}");

    def __repr__(self):
        print(f"Producto({self.nombre}, {self.precio}€ , {self.stock})")

    def __bol__(self):
            if self.stock == 0 and self.stock < 0:
                 return False;
            else: 
                return True;
    def __mul__(self,cantidad):
         return float(self.precio * cantidad);




