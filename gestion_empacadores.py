import tkinter as tk
from tkinter import ttk, messagebox
from gestion_paquetes import paquetes  # Importar la lista de paquetes

def empaquetar_producto():
    root = tk.Toplevel()
    root.title("Empaquetar Producto")

    window_width = 400
    window_height = 200
    root.geometry(f"{window_width}x{window_height}")

    centrar_ventana(root, window_width, window_height)

    tk.Label(root, text="ID del Producto:").grid(row=0, column=0, padx=10, pady=10)
    entry_id_producto = tk.Entry(root)
    entry_id_producto.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(root, text="Cliente:").grid(row=1, column=0, padx=10, pady=10)
    entry_cliente = tk.Entry(root)
    entry_cliente.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(root, text="Distribuidor:").grid(row=2, column=0, padx=10, pady=10)
    entry_distribuidor = tk.Entry(root)
    entry_distribuidor.grid(row=2, column=1, padx=10, pady=10)

    def confirmar_empaquetado():
        producto_id = int(entry_id_producto.get())  # Convertir a entero para ID
        cliente = entry_cliente.get()
        distribuidor = entry_distribuidor.get()

        nuevo_paquete = {
            "ID": producto_id,
            "Cliente": cliente,
            "Distribuidor": distribuidor,
            "Estado": "Pendiente",
            "Fase": "En almacén",
            "Fecha_Salida": "--",
            "Hora_Salida": ":",
            "Fecha_Llegada": "--",
            "Hora_Llegada": ":"
        }

        paquetes.append(nuevo_paquete)

        messagebox.showinfo("Éxito", f"Producto {producto_id} empaquetado con éxito para {cliente}. Estado: Pendiente")
        root.destroy()

    btn_confirmar = tk.Button(root, text="Confirmar Empaquetado", command=confirmar_empaquetado)
    btn_confirmar.grid(row=3, column=0, columnspan=2, pady=10)
    
    btn_cerrar = ttk.Button(root, text="Cerrar", command=root.destroy)
    btn_cerrar.grid(row=4, column=0, columnspan=2, pady=10)

def centrar_ventana(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    window.geometry(f"{width}x{height}+{x}+{y}")