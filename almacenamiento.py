import csv
import os

ARCHIVO_PRODUCTOS = "productos.csv"

def inicializar_archivo():
    if not os.path.exists(ARCHIVO_PRODUCTOS):
        with open(ARCHIVO_PRODUCTOS, mode='w', newline='', encoding='utf-8') as file:
            escritor = csv.writer(file)
            escritor.writerow(["id", "nombre", "descripcion", "precio", "cantidad"])

def limpiar_almacenamiento():
    """Limpia el archivo de almacenamiento, dejando solo los encabezados."""
    with open(ARCHIVO_PRODUCTOS, mode='w', newline='', encoding='utf-8') as file:
        escritor = csv.writer(file)
        escritor.writerow(["id", "nombre", "descripcion", "precio", "cantidad"])

def leer_productos():
    if not os.path.exists(ARCHIVO_PRODUCTOS):
        inicializar_archivo()
    with open(ARCHIVO_PRODUCTOS, mode='r', encoding='utf-8') as file:
        lector = csv.DictReader(file)
        return list(lector)

def crear_producto(nombre, descripcion, precio, cantidad):
    productos = leer_productos()
    ultimo_id = int(productos[-1]["id"]) if productos else 0
    nuevo_id = str(ultimo_id + 1)

    with open(ARCHIVO_PRODUCTOS, mode='a', newline='', encoding='utf-8') as file:
        escritor = csv.writer(file)
        escritor.writerow([nuevo_id, nombre, descripcion, precio, cantidad])

def actualizar_producto(id_producto, nombre, descripcion, precio, cantidad):
    productos = leer_productos()
    actualizado = False
    with open(ARCHIVO_PRODUCTOS, mode='w', newline='', encoding='utf-8') as file:
        escritor = csv.writer(file)
        escritor.writerow(["id", "nombre", "descripcion", "precio", "cantidad"])
        for producto in productos:
            if producto["id"] == id_producto:
                escritor.writerow([id_producto, nombre, descripcion, precio, cantidad])
                actualizado = True
            else:
                escritor.writerow(producto.values())
    return actualizado

def eliminar_producto(id_producto):
    productos = leer_productos()
    eliminado = False
    with open(ARCHIVO_PRODUCTOS, mode='w', newline='', encoding='utf-8') as file:
        escritor = csv.writer(file)
        escritor.writerow(["id", "nombre", "descripcion", "precio", "cantidad"])
        for producto in productos:
            if producto["id"] != id_producto:
                escritor.writerow(producto.values())
            else:
                eliminado = True
    return eliminado
