# Tabla hash: encadenamiento vs. direccionamiento abierto lineal

## 1. Descripción del problema

En un inventario con muchos productos, buscar un SKU recorriendo toda la lista
cuesta O(n). Una tabla hash permite insertar, buscar y eliminar productos en
tiempo promedio O(1), pero dos SKU distintos pueden caer en la misma posición
de la tabla (una **colisión**) y hay que resolverlo con alguna estrategia.

## 2. Objetivo del proyecto

Implementar manualmente, en Python y sin usar `dict`, `set` ni `hash()`, una
tabla hash con dos métodos de resolución de colisiones:

- **Encadenamiento** (separate chaining).
- **Direccionamiento abierto con sondeo lineal** (linear probing).

Ambos métodos ofrecen las operaciones **insertar, buscar y eliminar** sobre un
inventario de productos. Una aplicación de consola con menú aplica cada
operación a las dos tablas a la vez y muestra los resultados lado a lado, junto
con el número de comparaciones de cada una, para entender la diferencia entre
los dos métodos.

## 3. Datos

Datos **sintéticos, creados manualmente con fines didácticos**. No se utiliza
ninguna fuente externa.

| Campo      | Tipo   | Descripción                          |
|------------|--------|--------------------------------------|
| `sku`      | texto  | Código del producto. Es la **llave** |
| `nombre`   | texto  | Nombre del producto                  |
| `precio`   | número | Precio unitario                      |
| `cantidad` | entero | Unidades en inventario               |

Se precargan unos 12 productos (opción 5 del menú), elegidos para que algunos
SKU colisionen a propósito y la diferencia entre métodos se vea a simple vista.

## 4. Diseño

### Función hash (compartida)

Se suma el código `ord()` de cada carácter del SKU y se toma el módulo del
tamaño de la tabla. El tamaño es fijo (11 posiciones, un número primo y
pequeño para que las colisiones sean visibles). No se redimensiona.

Ejemplo de colisión: `"A1"` suma 65 + 49 = 114 y `"B0"` suma 66 + 48 = 114.
Con tamaño 11, ambos caen en la posición `114 % 11 = 4`.

### Encadenamiento

La tabla es una lista de 11 listas; cada posición guarda su propia cadena.

- **Insertar:** calcula el índice y recorre la cadena. Si el SKU existe, lo
  actualiza; si no, lo agrega.
- **Buscar:** calcula el índice y recorre solo esa cadena.
- **Eliminar:** busca en la cadena y quita el elemento.

### Sondeo lineal

La tabla es una lista de 11 casillas. Cada casilla es `None` (vacía),
`ELIMINADO` (marca) o un producto.

- **Insertar:** prueba las posiciones `(h + i) % 11`. Antes de reutilizar una
  marca `ELIMINADO`, verifica que el SKU no exista más adelante. Si recorre
  toda la tabla sin lugar, informa "tabla llena".
- **Buscar:** salta las marcas `ELIMINADO` y se detiene al encontrar `None`.
- **Eliminar:** deja la marca `ELIMINADO` en lugar de `None`. Si dejara `None`,
  se cortaría la búsqueda de los elementos que colisionaron después.

### Comparación

Ambas clases tienen la misma interfaz (`insertar`, `buscar`, `eliminar`,
`mostrar`) y cuentan las comparaciones de cada operación.

## 5. Estructura del proyecto

```
tabla_hash/
├── main.py                   # menú de consola
├── funcion_hash.py           # función hash compartida
├── hash_encadenamiento.py    # clase TablaEncadenada
├── hash_lineal.py            # clase TablaLineal
├── productos_demo.py         # productos precargados
├── test_*.py                 # pruebas con unittest
└── README.md
```

## 6. Cómo ejecutar

Requiere Python 3. No hay dependencias externas.

python main.py                     # ejecutar la app


### Menú

```
1. Insertar producto
2. Buscar producto por SKU
3. Eliminar producto
4. Mostrar tablas (con colisiones)
5. Cargar productos de demostración
0. Salir
```

## 7. Escenario de demostración

Este recorrido muestra por qué la marca `ELIMINADO` es necesaria:

1. Cargar los productos demo (opción 5).
2. Eliminar un SKU que tenga colisión (opción 3).
3. Buscar el SKU que colisionó con él (opción 2).
4. Mostrar las tablas (opción 4).

Resultado esperado: en la tabla de sondeo lineal aparece la marca `ELIMINADO`
y el segundo SKU **se sigue encontrando**. En encadenamiento, el segundo SKU
queda como único elemento de su cadena.

> Pega aquí la salida real de la app al terminar la implementación.

## 8. Conclusiones

> Completar al terminar: qué método hizo menos comparaciones en el escenario
> de demostración, qué pasó con la marca `ELIMINADO`, y cuándo conviene cada
> estrategia.
