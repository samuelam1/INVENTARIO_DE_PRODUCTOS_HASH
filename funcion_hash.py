TAMANHO = 11

def calcular_hash(sku,tamanho = TAMANHO):
    suma = 0
    for c in sku:
        suma += ord(c)
    return suma % tamanho
