import unittest
from almacenamiento import (
    inicializar_archivo,
    leer_productos,
    crear_producto,
    actualizar_producto,
    eliminar_producto,
    limpiar_almacenamiento  # Importar la función corregida
)

class TestCRUDOperaciones(unittest.TestCase):
    def setUp(self):
        """Se ejecuta antes de cada prueba: limpia el archivo y configura un producto inicial."""
        inicializar_archivo()
        limpiar_almacenamiento()  # Limpia los datos existentes en el archivo
        crear_producto("Producto de prueba", "Descripción de prueba", "10.50", "5")

    def test_leer_productos_exito(self):
        """Prueba que se puedan leer los productos correctamente."""
        productos = leer_productos()
        self.assertEqual(len(productos), 1)  # Debe haber 1 producto
        self.assertEqual(productos[0]["nombre"], "Producto de prueba")  # Validar nombre

    def test_crear_producto_exito(self):
        """Prueba que se pueda crear un producto correctamente."""
        crear_producto("Producto 2", "Descripción 2", "20.00", "10")
        productos = leer_productos()
        self.assertEqual(len(productos), 2)  # Ahora deben haber 2 productos
        self.assertEqual(productos[1]["nombre"], "Producto 2")  # Validar nombre del segundo producto

    def test_actualizar_producto_exito(self):
        """Prueba que se pueda actualizar un producto existente."""
        productos = leer_productos()
        id_producto = productos[0]["id"]
        actualizado = actualizar_producto(id_producto, "Producto actualizado", "Nueva descripción", "15.00", "3")
        self.assertTrue(actualizado)  # Debe devolver True porque la actualización tuvo éxito
        productos_actualizados = leer_productos()
        self.assertEqual(productos_actualizados[0]["nombre"], "Producto actualizado")  # Validar cambio

    def test_actualizar_producto_error(self):
        """Prueba que no se pueda actualizar un producto inexistente."""
        actualizado = actualizar_producto("999", "Producto inexistente", "Sin descripción", "0.00", "0")
        self.assertFalse(actualizado)  # Debe devolver False porque el producto no existe

    def test_eliminar_producto_exito(self):
        """Prueba que se pueda eliminar un producto existente."""
        productos = leer_productos()
        id_producto = productos[0]["id"]
        eliminado = eliminar_producto(id_producto)
        self.assertTrue(eliminado)  # Debe devolver True porque el producto fue eliminado
        productos_restantes = leer_productos()
        self.assertEqual(len(productos_restantes), 0)  # No deben quedar productos

    def test_eliminar_producto_error(self):
        """Prueba que no se pueda eliminar un producto inexistente."""
        eliminado = eliminar_producto("999")  # Intentar eliminar un ID inexistente
        self.assertFalse(eliminado)  # Debe devolver False porque el producto no existe

if __name__ == "__main__":
    unittest.main()
