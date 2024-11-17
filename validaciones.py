def validar_campos(nombre, descripcion, precio, cantidad):
    errores = []
    if not nombre.strip():
        errores.append("El nombre no puede estar vacío.")
    if not descripcion.strip():
        errores.append("La descripción no puede estar vacía.")
    try:
        precio = float(precio)
        if precio <= 0:
            errores.append("El precio debe ser mayor que 0.")
    except ValueError:
        errores.append("El precio debe ser un número válido.")
    try:
        cantidad = int(cantidad)
        if cantidad < 0:
            errores.append("La cantidad no puede ser negativa.")
    except ValueError:
        errores.append("La cantidad debe ser un número entero.")
    return errores
