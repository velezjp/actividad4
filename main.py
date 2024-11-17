from tkinter import Tk
from interfaz import AppProductos
from almacenamiento import inicializar_archivo

if __name__ == "__main__":
    inicializar_archivo()
    root = Tk()
    app = AppProductos(root)
    root.mainloop()
