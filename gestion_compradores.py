import tkinter as tk
from tkinter import ttk, messagebox

compradores = [
    {"ID": 1, "Nombre": "Juan", "Apellido": "Pérez", "Documento": "123456789", "Teléfono": "1234567890", "Dirección": "Calle 123", "Correo": "juan.perez@example.com"},
    {"ID": 2, "Nombre": "Ana", "Apellido": "García", "Documento": "987654321", "Teléfono": "0987654321", "Dirección": "Avenida 456", "Correo": "ana.garcia@example.com"},
]

def ver_compradores():
    root = tk.Toplevel()
    root.title("Ver Compradores")
    
    window_width = 600
    window_height = 350
    root.geometry(f"{window_width}x{window_height}")
    
    centrar_ventana(root, window_width, window_height)

    columns = ("ID", "Nombre", "Apellido", "Documento", "Teléfono", "Dirección", "Correo")
    tree = ttk.Treeview(root, columns=columns, show="headings")
    
    tree.heading("ID", text="ID")
    tree.heading("Nombre", text="Nombre")
    tree.heading("Apellido", text="Apellido")
    tree.heading("Documento", text="Documento")
    tree.heading("Teléfono", text="Teléfono")
    tree.heading("Dirección", text="Dirección")
    tree.heading("Correo", text="Correo")
    
    tree.column("ID", width=30, anchor='center')
    tree.column("Nombre", width=70, anchor='center')
    tree.column("Apellido", width=70, anchor='center')
    tree.column("Documento", width=70, anchor='center')
    tree.column("Teléfono", width=70, anchor='center')
    tree.column("Dirección", width=130, anchor='center')
    tree.column("Correo", width=130, anchor='center')
    
    for comprador in compradores:
        tree.insert("", tk.END, values=(comprador["ID"], comprador["Nombre"], comprador["Apellido"], comprador["Documento"], comprador["Teléfono"], comprador["Dirección"], comprador["Correo"]))

    tree.pack(fill="both", expand=True)

    btn_agregar = ttk.Button(root, text="Agregar Comprador", command=agregar_comprador)
    btn_agregar.pack(side="left", padx=10, pady=10)

    btn_editar = ttk.Button(root, text="Editar Comprador", command=lambda: editar_comprador(tree))
    btn_editar.pack(side="left", padx=10, pady=10)

    btn_eliminar = ttk.Button(root, text="Eliminar Comprador", command=lambda: eliminar_comprador(tree))
    btn_eliminar.pack(side="left", padx=10, pady=10)

    cerrar_btn = ttk.Button(root, text="Cerrar", command=root.destroy)
    cerrar_btn.pack(pady=10)

def agregar_comprador():
    root = tk.Toplevel()
    root.title("Agregar Nuevo Comprador")

    window_width = 400
    window_height = 300
    root.geometry(f"{window_width}x{window_height}")

    centrar_ventana(root, window_width, window_height)

    tk.Label(root, text="Nombre:").grid(row=0, column=0, padx=10, pady=10)
    entry_nombre = tk.Entry(root)
    entry_nombre.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(root, text="Apellido:").grid(row=1, column=0, padx=10, pady=10)
    entry_apellido = tk.Entry(root)
    entry_apellido.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(root, text="Documento:").grid(row=2, column=0, padx=10, pady=10)
    entry_documento = tk.Entry(root)
    entry_documento.grid(row=2, column=1, padx=10, pady=10)

    tk.Label(root, text="Teléfono:").grid(row=3, column=0, padx=10, pady=10)
    entry_telefono = tk.Entry(root)
    entry_telefono.grid(row=3, column=1, padx=10, pady=10)

    tk.Label(root, text="Dirección:").grid(row=4, column=0, padx=10, pady=10)
    entry_direccion = tk.Entry(root)
    entry_direccion.grid(row=4, column=1, padx=10, pady=10)

    tk.Label(root, text="Correo:").grid(row=5, column=0, padx=10, pady=10)
    entry_correo = tk.Entry(root)
    entry_correo.grid(row=5, column=1, padx=10, pady=10)

    def guardar_comprador():
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        documento = entry_documento.get()
        telefono = entry_telefono.get()
        direccion = entry_direccion.get()
        correo = entry_correo.get()

        if nombre and apellido and documento and telefono and direccion and correo:
            nuevo_comprador = {"ID": len(compradores) + 1, "Nombre": nombre, "Apellido": apellido, "Documento": documento, "Teléfono": telefono, "Dirección": direccion, "Correo": correo}
            compradores.append(nuevo_comprador)

            messagebox.showinfo("Éxito", "Comprador agregado con éxito")
            root.destroy()
            ver_compradores()
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios")

    btn_guardar = tk.Button(root, text="Guardar", command=guardar_comprador)
    btn_guardar.grid(row=6, column=0, columnspan=2, pady=10)

def editar_comprador(tree):
    selected_item = tree.selection()
    if selected_item:
        comprador_info = tree.item(selected_item)["values"]
        comprador_id = comprador_info[0]
        
        comprador = next((c for c in compradores if c["ID"] == comprador_id), None)
        
        if comprador:
            root = tk.Toplevel()
            root.title("Editar Comprador")

            window_width = 400
            window_height = 300
            root.geometry(f"{window_width}x{window_height}")

            centrar_ventana(root, window_width, window_height)

            tk.Label(root, text="Nombre:").grid(row=0, column=0, padx=10, pady=10)
            entry_nombre = tk.Entry(root)
            entry_nombre.grid(row=0, column=1, padx=10, pady=10)
            entry_nombre.insert(0, comprador["Nombre"])

            tk.Label(root, text="Apellido:").grid(row=1, column=0, padx=10, pady=10)
            entry_apellido = tk.Entry(root)
            entry_apellido.grid(row=1, column=1, padx=10, pady=10)
            entry_apellido.insert(0, comprador["Apellido"])

            tk.Label(root, text="Documento:").grid(row=2, column=0, padx=10, pady=10)
            entry_documento = tk.Entry(root)
            entry_documento.grid(row=2, column=1, padx=10, pady=10)
            entry_documento.insert(0, comprador["Documento"])

            tk.Label(root, text="Teléfono:").grid(row=3, column=0, padx=10, pady=10)
            entry_telefono = tk.Entry(root)
            entry_telefono.grid(row=3, column=1, padx=10, pady=10)
            entry_telefono.insert(0, comprador["Teléfono"])

            tk.Label(root, text="Dirección:").grid(row=4, column=0, padx=10, pady=10)
            entry_direccion = tk.Entry(root)
            entry_direccion.grid(row=4, column=1, padx=10, pady=10)
            entry_direccion.insert(0, comprador["Dirección"])

            tk.Label(root, text="Correo:").grid(row=5, column=0, padx=10, pady=10)
            entry_correo = tk.Entry(root)
            entry_correo.grid(row=5, column=1, padx=10, pady=10)
            entry_correo.insert(0, comprador["Correo"])

            def guardar_cambios():
                comprador["Nombre"] = entry_nombre.get()
                comprador["Apellido"] = entry_apellido.get()
                comprador["Documento"] = entry_documento.get()
                comprador["Teléfono"] = entry_telefono.get()
                comprador["Dirección"] = entry_direccion.get()
                comprador["Correo"] = entry_correo.get()

                tree.item(selected_item, values=(comprador["ID"], comprador["Nombre"], comprador["Apellido"], comprador["Documento"], comprador["Teléfono"], comprador["Dirección"], comprador["Correo"]))
                messagebox.showinfo("Éxito", "Comprador actualizado con éxito")
                root.destroy()

            btn_guardar = tk.Button(root, text="Guardar Cambios", command=guardar_cambios)
            btn_guardar.grid(row=6, column=0, columnspan=2, pady=10)
        else:
            messagebox.showerror("Error", "Comprador no encontrado")
    else:
        messagebox.showerror("Error", "Seleccione un comprador para editar")

def eliminar_comprador(tree):
    selected_item = tree.selection()
    if selected_item:
        comprador_info = tree.item(selected_item)["values"]
        comprador_id = comprador_info[0]
        
        confirm = messagebox.askyesno("Confirmar Eliminación", "¿Está seguro de que desea eliminar este comprador?")
        
        if confirm:
            global compradores
            compradores = [c for c in compradores if c["ID"] != comprador_id]

            tree.delete(selected_item)
            messagebox.showinfo("Éxito", "Comprador eliminado con éxito")
    else:
        messagebox.showerror("Error", "Seleccione un comprador para eliminar")

def centrar_ventana(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    window.geometry(f"{width}x{height}+{x}+{y}")