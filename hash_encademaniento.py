from funcion_hash import TAMANHO, calcular_hash

class Nodo: 
    def __init__(self,sku,nombre,precio,cantidad):
        self.sku = sku
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.siguiente = None
        
class TablaEncadenada:
    def __init__(self):
        self.cadenas = [None] * TAMANHO
        self.comparaciones = 0
        
    def insertar (self,sku, nombre, precio, cantidad):
        self.comparaciones = 0
        posicion = calcular_hash(sku)
        actual = self.cadenas[posicion]
        ultimo = None
        
        while actual is not None:
            self.comparaciones += 1
            
            if actual.sku == sku:
                actual.nombre = nombre
                actual.precio = precio
                actual.cantidad = cantidad
                return "actualizado"
            ultimo = actual
            actual = actual.siguiente
            
        nuevo = Nodo(sku, nombre,precio,cantidad)
        if ultimo is None:
            self.cadenas[posicion] = nuevo
        else:
            ultimo.siguiente = nuevo
        return "insertado"
    
    def buscar(self,sku):
        self.comparaciones = 0
        actual = self.cadenas[calcular_hash(sku)]
        
        while actual is not None:
            self.comparaciones += 1
            
            if actual.sku == sku:
                return actual
            actual = actual.siguiente
            
        return None
    
    def eliminar(self,sku):
        self.comparaciones = 0
        posicion = calcular_hash(sku)
        actual = self.cadenas[posicion]
        anterior = None
        while actual is not None:
            self.comparaciones += 1
            if actual.sku == sku:
                if anterior is None:
                    self.cadenas[posicion] = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False 
    
    def mostrar (self):
        texto = ""
        for i in range(TAMANHO):
            linea = str(i).rjust(2) + ": "
            nodos = 0
            actual = self.cadenas[i]
            while actual is not None:
                linea += "[" + actual.sku +"] ->"
                nodos += 1
                actual = actual.siguiente
            linea += "None"
            if nodos > 1:
                linea += "  (colisión)"
            if i > 0:
                texto += "\n"
            texto += linea
        return texto
        
        
    


    

        
