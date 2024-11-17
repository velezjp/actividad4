import tkinter as tk
from tkinter import ttk, messagebox
from almacenamiento import leer_productos, crear_producto, actualizar_producto, eliminar_producto
from validaciones import validar_campos

class AppProductos:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Productos")
        self.root.geometry("800x600")
        self.configurar_interfaz()

    def configurar_interfaz(self):
        self.tabla = ttk.Treeview(self.root, columns=("id", "nombre", "descripcion", "precio", "cantidad"), show='headings')
        self.tabla.heading("id", text="ID")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("descripcion", text="Descripción")
        self.tabla.heading("precio", text="Precio")
        self.tabla.heading("cantidad", text="Cantidad")
        self.tabla.pack(fill=tk.BOTH, expand=True)
        self.tabla.bind("<Double-1>", self.editar_producto)

        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=10)
        tk.Button(frame_botones, text="Agregar Producto", command=self.agregar_producto).grid(row=0, column=0, padx=5)
        tk.Button(frame_botones, text="Eliminar Producto", command=self.eliminar_producto).grid(row=0, column=1, padx=5)
        tk.Button(frame_botones, text="Actualizar Tabla", command=self.cargar_tabla).grid(row=0, column=2, padx=5)

        self.cargar_tabla()

    def cargar_tabla(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        for producto in leer_productos():
            self.tabla.insert("", tk.END, values=list(producto.values()))

    def agregar_producto(self):
        def guardar():
            errores = validar_campos(entry_nombre.get(), entry_descripcion.get(), entry_precio.get(), entry_cantidad.get())
            if errores:
                messagebox.showerror("Errores en los datos", "\n".join(errores))
                return

            crear_producto(entry_nombre.get(), entry_descripcion.get(), entry_precio.get(), entry_cantidad.get())
            self.cargar_tabla()
            ventana.destroy()

        ventana = tk.Toplevel(self.root)
        ventana.title("Agregar Producto")
        self.centrar_ventana(ventana, 400, 300)

        tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(ventana, text="Descripción:").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(ventana, text="Precio:").grid(row=2, column=0, padx=10, pady=10)
        tk.Label(ventana, text="Cantidad:").grid(row=3, column=0, padx=10, pady=10)
        entry_nombre = tk.Entry(ventana, width=30)
        entry_descripcion = tk.Entry(ventana, width=30)
        entry_precio = tk.Entry(ventana, width=30)
        entry_cantidad = tk.Entry(ventana, width=30)
        entry_nombre.grid(row=0, column=1, padx=10, pady=10)
        entry_descripcion.grid(row=1, column=1, padx=10, pady=10)
        entry_precio.grid(row=2, column=1, padx=10, pady=10)
        entry_cantidad.grid(row=3, column=1, padx=10, pady=10)
        tk.Button(ventana, text="Guardar", command=guardar).grid(row=4, column=0, columnspan=2, pady=20)

    def editar_producto(self, event):
        item = self.tabla.selection()[0]
        valores = self.tabla.item(item, "values")

        def guardar():
            errores = validar_campos(entry_nombre.get(), entry_descripcion.get(), entry_precio.get(), entry_cantidad.get())
            if errores:
                messagebox.showerror("Errores en los datos", "\n".join(errores))
                return

            actualizar_producto(valores[0], entry_nombre.get(), entry_descripcion.get(), entry_precio.get(), entry_cantidad.get())
            self.cargar_tabla()
            ventana.destroy()

        ventana = tk.Toplevel(self.root)
        ventana.title("Editar Producto")
        self.centrar_ventana(ventana, 400, 300)

        tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(ventana, text="Descripción:").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(ventana, text="Precio:").grid(row=2, column=0, padx=10, pady=10)
        tk.Label(ventana, text="Cantidad:").grid(row=3, column=0, padx=10, pady=10)
        entry_nombre = tk.Entry(ventana, width=30)
        entry_descripcion = tk.Entry(ventana, width=30)
        entry_precio = tk.Entry(ventana, width=30)
        entry_cantidad = tk.Entry(ventana, width=30)
        entry_nombre.insert(0, valores[1])
        entry_descripcion.insert(0, valores[2])
        entry_precio.insert(0, valores[3])
        entry_cantidad.insert(0, valores[4])
        entry_nombre.grid(row=0, column=1, padx=10, pady=10)
        entry_descripcion.grid(row=1, column=1, padx=10, pady=10)
        entry_precio.grid(row=2, column=1, padx=10, pady=10)
        entry_cantidad.grid(row=3, column=1, padx=10, pady=10)
        tk.Button(ventana, text="Guardar", command=guardar).grid(row=4, column=0, columnspan=2, pady=20)

    def eliminar_producto(self):
        seleccionado = self.tabla.selection()
        if not seleccionado:
            messagebox.showerror("Error", "Seleccione un producto")
            return
        id_producto = self.tabla.item(seleccionado[0], "values")[0]
        if eliminar_producto(id_producto):
            messagebox.showinfo("Éxito", "Producto eliminado")
        else:
            messagebox.showerror("Error", "No se pudo eliminar el producto")
        self.cargar_tabla()

    def centrar_ventana(self, ventana, ancho, alto):
        ventana.update_idletasks()
        ancho_pantalla = ventana.winfo_screenwidth()
        alto_pantalla = ventana.winfo_screenheight()
        x = (ancho_pantalla - ancho) // 2
        y = (alto_pantalla - alto) // 2
        ventana.geometry(f"{ancho}x{alto}+{x}+{y}")
