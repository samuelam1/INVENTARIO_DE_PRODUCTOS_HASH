from hash_encademaniento import TablaEncadenada
from hash_lineal import TablaLineal
from productos_demo import PRODUCTOS_DEMO


def convertir_precio(texto):
    """Devuelve el precio como número, o None si no es válido (vacío, texto, negativo)."""
    texto = texto.strip()
    if texto == "":
        return None
    puntos = 0
    for caracter in texto:
        if caracter == ".":
            puntos += 1
        elif caracter < "0" or caracter > "9":
            return None
    if puntos > 1 or texto == ".":
        return None
    if puntos == 1:
        return float(texto)
    return int(texto)


def convertir_cantidad(texto):
    """Devuelve la cantidad como entero, o None si no es válida."""
    texto = texto.strip()
    if texto == "":
        return None
    for caracter in texto:
        if caracter < "0" or caracter > "9":
            return None
    return int(texto)


def lado_a_lado(izquierda, derecha, ancho=None):
    """Une dos textos de varias líneas en dos columnas separadas por '|'."""
    lineas_izq = izquierda.split("\n")
    lineas_der = derecha.split("\n")
    if ancho is None:  # por defecto, la línea más larga de la izquierda
        ancho = 0
        for linea in lineas_izq:
            if len(linea) > ancho:
                ancho = len(linea)
    total = max(len(lineas_izq), len(lineas_der))
    resultado = ""
    for i in range(total):
        izq = lineas_izq[i] if i < len(lineas_izq) else ""
        der = lineas_der[i] if i < len(lineas_der) else ""
        if i > 0:
            resultado += "\n"
        resultado += izq.ljust(ancho) + " | " + der
    return resultado


def descripcion(producto):
    return (
        producto.sku
        + " - "
        + producto.nombre
        + ", precio "
        + str(producto.precio)
        + ", cantidad "
        + str(producto.cantidad)
    )


def resultado_dos_columnas(titulo_izq, texto_izq, titulo_der, texto_der):
    return lado_a_lado(titulo_izq + "\n" + texto_izq, titulo_der + "\n" + texto_der)


def insertar(enc, lin, sku, nombre, precio, cantidad):
    estado_enc = enc.insertar(sku, nombre, precio, cantidad)
    estado_lin = lin.insertar(sku, nombre, precio, cantidad)
    return resultado_dos_columnas(
        "Encadenamiento",
        estado_enc + " (" + str(enc.comparaciones) + " comparaciones)",
        "Sondeo lineal",
        estado_lin + " (" + str(lin.comparaciones) + " comparaciones)",
    )


def buscar(enc, lin, sku):
    encontrado_enc = enc.buscar(sku)
    comp_enc = enc.comparaciones
    encontrado_lin = lin.buscar(sku)
    comp_lin = lin.comparaciones
    texto_enc = descripcion(encontrado_enc) if encontrado_enc else "no encontrado"
    texto_lin = descripcion(encontrado_lin) if encontrado_lin else "no encontrado"
    return resultado_dos_columnas(
        "Encadenamiento",
        texto_enc + " (" + str(comp_enc) + " comparaciones)",
        "Sondeo lineal",
        texto_lin + " (" + str(comp_lin) + " comparaciones)",
    )


def eliminar(enc, lin, sku):
    ok_enc = enc.eliminar(sku)
    comp_enc = enc.comparaciones
    ok_lin = lin.eliminar(sku)
    comp_lin = lin.comparaciones
    texto_enc = "eliminado" if ok_enc else "no encontrado"
    texto_lin = "eliminado" if ok_lin else "no encontrado"
    return resultado_dos_columnas(
        "Encadenamiento",
        texto_enc + " (" + str(comp_enc) + " comparaciones)",
        "Sondeo lineal",
        texto_lin + " (" + str(comp_lin) + " comparaciones)",
    )


def mostrar(enc, lin):
    return resultado_dos_columnas(
        "Encadenamiento", enc.mostrar(), "Sondeo lineal", lin.mostrar()
    )


def cargar_demo(enc, lin):
    """Inserta los productos demo en ambas tablas. Devuelve un resultado por producto."""
    resultados = []
    for sku, nombre, precio, cantidad in PRODUCTOS_DEMO:
        estado_enc = enc.insertar(sku, nombre, precio, cantidad)
        estado_lin = lin.insertar(sku, nombre, precio, cantidad)
        resultados.append(
            sku + ": encadenamiento " + estado_enc + " | lineal " + estado_lin
        )
    return resultados


def pedir_sku():
    sku = input("SKU: ").strip()
    if sku == "":
        print("El SKU no puede estar vacío.")
        return None
    return sku


def opcion_insertar(enc, lin):
    sku = pedir_sku()
    if sku is None:
        return
    nombre = input("Nombre: ").strip()
    if nombre == "":
        print("El nombre no puede estar vacío.")
        return
    precio = convertir_precio(input("Precio: "))
    if precio is None:
        print("Precio inválido: debe ser un número positivo.")
        return
    cantidad = convertir_cantidad(input("Cantidad: "))
    if cantidad is None:
        print("Cantidad inválida: debe ser un entero positivo.")
        return
    print(insertar(enc, lin, sku, nombre, precio, cantidad))


def main():
    enc = TablaEncadenada()
    lin = TablaLineal()
    while True:
        print("\n1. Insertar producto")
        print("2. Buscar producto por SKU")
        print("3. Eliminar producto")
        print("4. Mostrar tablas (con colisiones)")
        print("5. Cargar productos de demostración")
        print("0. Salir")
        opcion = input("Opción: ").strip()
        if opcion == "1":
            opcion_insertar(enc, lin)
        elif opcion == "2":
            sku = pedir_sku()
            if sku is not None:
                print(buscar(enc, lin, sku))
        elif opcion == "3":
            sku = pedir_sku()
            if sku is not None:
                print(eliminar(enc, lin, sku))
        elif opcion == "4":
            print(mostrar(enc, lin))
        elif opcion == "5":
            for linea in cargar_demo(enc, lin):
                print(linea)
        elif opcion == "0":
            print("Adiós.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()