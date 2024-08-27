import tkinter as tk
from tkinter import ttk

def ver_importaciones():
    root = tk.Toplevel()
    root.title("Ver Importaciones")

    window_width = 600
    window_height = 400
    root.geometry(f"{window_width}x{window_height}")

    centrar_ventana(root, window_width, window_height)

    columns = ("ID", "Producto", "Proveedor", "Estado", "Fecha de Importación")
    
    container = ttk.Frame(root)
    container.pack(fill="both", expand=True)

    tree = ttk.Treeview(container, columns=columns, show="headings")
    tree.pack(fill="both", expand=True)

    tree.heading("ID", text="ID")
    tree.column("ID", width=30, anchor='center')

    tree.heading("Producto", text="Producto")
    tree.column("Producto", width=70, anchor='center')

    tree.heading("Proveedor", text="Proveedor")
    tree.column("Proveedor", width=70, anchor='center')

    tree.heading("Estado", text="Estado")
    tree.column("Estado", width=70, anchor='center')

    tree.heading("Fecha de Importación", text="Fecha de Importación")
    tree.column("Fecha de Importación", width=70, anchor='center')

    importaciones = [
        {"ID": 1, "Producto": "Producto A", "Proveedor": "Proveedor X", "Estado": "En proceso", "Fecha de Importación": "2024-08-20"},
        {"ID": 2, "Producto": "Producto B", "Proveedor": "Proveedor Y", "Estado": "Completado", "Fecha de Importación": "2024-08-19"},
    ]

    for imp in importaciones:
        tree.insert("", tk.END, values=(imp["ID"], imp["Producto"], imp["Proveedor"], imp["Estado"], imp["Fecha de Importación"]))

    btn_cerrar = ttk.Button(root, text="Cerrar", command=root.destroy)
    btn_cerrar.pack(pady=10)

def centrar_ventana(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    window.geometry(f"{width}x{height}+{x}+{y}")