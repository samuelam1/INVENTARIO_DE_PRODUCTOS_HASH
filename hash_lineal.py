
from funcion_hash import TAMANHO, calcular_hash

ELIMINADO = "ELIMINADO"

class producto:
    
    def __init__(self, sku, nombre, precio, cantidad):
        self.sku = sku
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        
class TablaLineal:
    
    def __init__(self):   
        self.casillas = [None] * TAMANHO
        self.comparaciones = 0
        
    def insertar(self,sku,nombre,precio,cantidad):
        self.comparaciones = 0
        h = calcular_hash(sku)
        primer_eliminado = None
        destino = None
            
        for i in range(TAMANHO):
            posicion = (h + i) % TAMANHO
            casilla = self.casillas[posicion]
                
            if casilla is None:
                destino = posicion
                break
                
            if casilla is ELIMINADO:
                if primer_eliminado is None:
                    primer_eliminado = posicion
                continue
            self.comparaciones += 1
                
            if casilla.sku == sku:  
                casilla.nombre = nombre
                casilla.precio = precio
                casilla.cantidad = cantidad
                return "actualizado"
        # ya se comprobó que el SKU no existe: ahora sí se puede reutilizar
        if primer_eliminado is not None:
            destino = primer_eliminado
            
        if destino is None:
            return "Tabla llena"
        self.casillas[destino] = producto(sku, nombre, precio, cantidad)
        return "insertado"
    
    def buscar(self, sku):
        self.comparaciones = 0
        h = calcular_hash(sku)
        for i in range(TAMANHO):
            casilla = self.casillas[(h + i) % TAMANHO]
            if casilla is None:
                return None
            if casilla is ELIMINADO:
                continue
            self.comparaciones += 1
            if casilla.sku == sku:
                return casilla
        return None
    
    def eliminar(self,sku):
        self.comparaciones = 0 
        h = calcular_hash(sku)
        for i in range(TAMANHO):
            posicion = (h + i) % TAMANHO
            casilla = self.casillas[posicion]
            
            if casilla is None:
                return False
            if casilla is ELIMINADO:
                continue
            self.comparaciones += 1
            if casilla.sku == sku:
                self.casillas[posicion] = ELIMINADO
                return True
        return False
    
    def mostrar (self):
        texto = ""
        for i in range(TAMANHO):
            linea = str(i).rjust(2) + ": "
            casilla = self.casillas[i]
            if casilla is None:
                linea += "None"
            elif casilla is ELIMINADO:
                linea += ELIMINADO
            else:
                linea += "[" + casilla.sku + "]"
                if calcular_hash(casilla.sku) != i:
                    linea += " (colisión)"
            if i > 0:
                texto += "\n"
            texto += linea
        return texto