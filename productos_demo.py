# Productos de demostración (datos sintéticos). Varios SKU colisionan a propósito.
# Formato: (sku, nombre, precio, cantidad)

PRODUCTOS_DEMO = [
    ("A100", "Tornillo", 500, 200),    # hash 1
    ("A010", "Tuerca", 300, 150),      # hash 1 (colisiona con A100)
    ("A001", "Arandela", 100, 400),    # hash 1 (colisiona)
    ("B200", "Martillo", 25000, 12),   # hash 3
    ("B020", "Destornillador", 18000, 20),  # hash 3 (colisiona)
    ("C300", "Taladro", 250000, 5),    # hash 5
    ("C030", "Sierra", 40000, 8),      # hash 5 (colisiona)
    ("D400", "Cinta métrica", 9000, 30),  # hash 7
    ("F600", "Guantes", 7000, 50),     # hash 0
    ("AB1", "Pintura", 60000, 10),     # hash 4
    ("BA1", "Brocha", 6000, 25),       # hash 4 (colisiona)
    ("LLA01", "Llanta", 800000, 4),    # hash 6; el 12.º producto llena la tabla lineal
]
