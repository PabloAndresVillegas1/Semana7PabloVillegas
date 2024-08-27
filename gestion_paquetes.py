import tkinter as tk
from tkinter import ttk, messagebox

paquetes = [
    {"ID": 1, "Cliente": "Cliente A", "Distribuidor": "Distribuidor X", "Estado": "Pendiente", "Fase": "En almacén", "Fecha_Salida": "--", "Hora_Salida": ":", "Fecha_Llegada": "--", "Hora_Llegada": ":"},
    {"ID": 2, "Cliente": "Cliente B", "Distribuidor": "Distribuidor Y", "Estado": "Aceptado", "Fase": "En ruta", "Fecha_Salida": "2024-08-24", "Hora_Salida": "14:00", "Fecha_Llegada": "2024-08-29", "Hora_Llegada": "09:00"},
]

def ver_paquetes():
    root = tk.Toplevel()
    root.title("Ver Paquetes")

    window_width = 700
    window_height = 400
    root.geometry(f"{window_width}x{window_height}")

    centrar_ventana(root, window_width, window_height)

    columns = ("ID", "Cliente", "Distribuidor", "Estado", "Fase", "Fecha_Salida", "Hora_Salida", "Fecha_Llegada", "Hora_Llegada")
    tree = ttk.Treeview(root, columns=columns, show="headings")

    column_widths = {
        "ID": 30,
        "Cliente": 70,
        "Distribuidor": 100,
        "Estado": 70,
        "Fase": 70,
        "Fecha_Salida": 70,
        "Hora_Salida": 70,
        "Fecha_Llegada": 70,
        "Hora_Llegada": 70
    }
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=column_widths.get(col, 100), anchor='center')

    for paquete in paquetes:
        tree.insert("", tk.END, values=(paquete["ID"], paquete["Cliente"], paquete["Distribuidor"], paquete["Estado"], paquete["Fase"], paquete["Fecha_Salida"], paquete["Hora_Salida"], paquete["Fecha_Llegada"], paquete["Hora_Llegada"]))

    tree.pack(fill="both", expand=True)

    btn_aceptar = ttk.Button(root, text="Aceptar Paquete", command=lambda: aceptar_paquete(tree))
    btn_aceptar.pack(side="left", padx=10, pady=10)

    btn_cancelar = ttk.Button(root, text="Cancelar Paquete", command=lambda: cancelar_paquete(tree))
    btn_cancelar.pack(side="left", padx=10, pady=10)

    btn_cambiar_datos = ttk.Button(root, text="Cambiar Datos", command=lambda: cambiar_datos(tree))
    btn_cambiar_datos.pack(side="left", padx=10, pady=10)

    btn_cambiar_fase = ttk.Button(root, text="Cambiar Fase", command=lambda: cambiar_fase(tree))
    btn_cambiar_fase.pack(side="left", padx=10, pady=10)

    btn_cambiar_fechas = ttk.Button(root, text="Cambiar Fechas y Horarios", command=lambda: cambiar_fechas(tree))
    btn_cambiar_fechas.pack(side="left", padx=10, pady=10)

    cerrar_btn = ttk.Button(root, text="Cerrar", command=root.destroy)
    cerrar_btn.pack(pady=10)

def aceptar_paquete(tree):
    selected_item = tree.selection()
    if selected_item:
        paquete_info = tree.item(selected_item)["values"]
        paquete_id = paquete_info[0]

        paquete = next((p for p in paquetes if p["ID"] == paquete_id), None)
        if paquete:
            paquete["Estado"] = "Aceptado"
            tree.item(selected_item, values=(paquete["ID"], paquete["Cliente"], paquete["Distribuidor"], paquete["Estado"], paquete["Fase"], paquete["Fecha_Salida"], paquete["Hora_Salida"], paquete["Fecha_Llegada"], paquete["Hora_Llegada"]))
            messagebox.showinfo("Éxito", "Paquete aceptado con éxito")
        else:
            messagebox.showerror("Error", "Paquete no encontrado")
    else:
        messagebox.showerror("Error", "Seleccione un paquete para aceptar")

def cancelar_paquete(tree):
    selected_item = tree.selection()
    if selected_item:
        paquete_info = tree.item(selected_item)["values"]
        paquete_id = paquete_info[0]

        confirm = messagebox.askyesno("Confirmar Cancelación", "¿Está seguro de que desea cancelar este paquete?")

        if confirm:
            global paquetes
            paquetes = [p for p in paquetes if p["ID"] != paquete_id]

            tree.delete(selected_item)
            messagebox.showinfo("Éxito", "Paquete cancelado con éxito")
    else:
        messagebox.showerror("Error", "Seleccione un paquete para cancelar")

def cambiar_datos(tree):
    selected_item = tree.selection()
    if selected_item:
        paquete_info = tree.item(selected_item)["values"]
        paquete_id = paquete_info[0]
        
        paquete = next((p for p in paquetes if p["ID"] == paquete_id), None)

        if paquete:
            root = tk.Toplevel()
            root.title("Cambiar Datos del Paquete")

            window_width = 300
            window_height = 250
            root.geometry(f"{window_width}x{window_height}")

            centrar_ventana(root, window_width, window_height)

            tk.Label(root, text="Cliente:").grid(row=0, column=0, padx=10, pady=10)
            entry_cliente = tk.Entry(root)
            entry_cliente.grid(row=0, column=1, padx=10, pady=10)
            entry_cliente.insert(0, paquete["Cliente"])

            tk.Label(root, text="Distribuidor:").grid(row=1, column=0, padx=10, pady=10)
            entry_distribuidor = tk.Entry(root)
            entry_distribuidor.grid(row=1, column=1, padx=10, pady=10)
            entry_distribuidor.insert(0, paquete["Distribuidor"])

            def guardar_cambios():
                paquete["Cliente"] = entry_cliente.get()
                paquete["Distribuidor"] = entry_distribuidor.get()

                tree.item(selected_item, values=(paquete["ID"], paquete["Cliente"], paquete["Distribuidor"], paquete["Estado"], paquete["Fase"], paquete["Fecha_Salida"], paquete["Hora_Salida"], paquete["Fecha_Llegada"], paquete["Hora_Llegada"]))
                messagebox.showinfo("Éxito", "Datos actualizados con éxito")
                root.destroy()

            btn_guardar = tk.Button(root, text="Guardar Cambios", command=guardar_cambios)
            btn_guardar.grid(row=2, column=0, columnspan=2, pady=10)
        else:
            messagebox.showerror("Error", "Paquete no encontrado")
    else:
        messagebox.showerror("Error", "Seleccione un paquete para cambiar datos")

def cambiar_fase(tree):
    selected_item = tree.selection()
    if selected_item:
        paquete_info = tree.item(selected_item)["values"]
        paquete_id = paquete_info[0]

        paquete = next((p for p in paquetes if p["ID"] == paquete_id), None)

        if paquete:
            root = tk.Toplevel()
            root.title("Cambiar Fase del Paquete")

            window_width = 300
            window_height = 150
            root.geometry(f"{window_width}x{window_height}")

            centrar_ventana(root, window_width, window_height)

            tk.Label(root, text="Nueva Fase:").grid(row=0, column=0, padx=10, pady=10)
            entry_fase = tk.Entry(root)
            entry_fase.grid(row=0, column=1, padx=10, pady=10)
            entry_fase.insert(0, paquete["Fase"])

            def guardar_fase():
                paquete["Fase"] = entry_fase.get()

                tree.item(selected_item, values=(paquete["ID"], paquete["Cliente"], paquete["Distribuidor"], paquete["Estado"], paquete["Fase"], paquete["Fecha_Salida"], paquete["Hora_Salida"], paquete["Fecha_Llegada"], paquete["Hora_Llegada"]))
                messagebox.showinfo("Éxito", "Fase actualizada con éxito")
                root.destroy()

            btn_guardar = tk.Button(root, text="Guardar Cambios", command=guardar_fase)
            btn_guardar.grid(row=1, column=0, columnspan=2, pady=10)
        else:
            messagebox.showerror("Error", "Paquete no encontrado")
    else:
        messagebox.showerror("Error", "Seleccione un paquete para cambiar fase")

def cambiar_fechas(tree):
    selected_item = tree.selection()
    if selected_item:
        paquete_info = tree.item(selected_item)["values"]
        paquete_id = paquete_info[0]

        paquete = next((p for p in paquetes if p["ID"] == paquete_id), None)

        if paquete:
            root = tk.Toplevel()
            root.title("Cambiar Fechas y Horarios del Paquete")

            window_width = 300
            window_height = 250
            root.geometry(f"{window_width}x{window_height}")

            centrar_ventana(root, window_width, window_height)

            tk.Label(root, text="Fecha de Salida (YYYY-MM-DD):").grid(row=0, column=0, padx=10, pady=10)
            entry_fecha_salida = tk.Entry(root)
            entry_fecha_salida.grid(row=0, column=1, padx=10, pady=10)
            entry_fecha_salida.insert(0, paquete["Fecha_Salida"])

            tk.Label(root, text="Hora de Salida (HH:MM):").grid(row=1, column=0, padx=10, pady=10)
            entry_hora_salida = tk.Entry(root)
            entry_hora_salida.grid(row=1, column=1, padx=10, pady=10)
            entry_hora_salida.insert(0, paquete["Hora_Salida"])

            tk.Label(root, text="Fecha de Llegada (YYYY-MM-DD):").grid(row=2, column=0, padx=10, pady=10)
            entry_fecha_llegada = tk.Entry(root)
            entry_fecha_llegada.grid(row=2, column=1, padx=10, pady=10)
            entry_fecha_llegada.insert(0, paquete["Fecha_Llegada"])

            tk.Label(root, text="Hora de Llegada (HH:MM):").grid(row=3, column=0, padx=10, pady=10)
            entry_hora_llegada = tk.Entry(root)
            entry_hora_llegada.grid(row=3, column=1, padx=10, pady=10)
            entry_hora_llegada.insert(0, paquete["Hora_Llegada"])

            def guardar_fechas():
                paquete["Fecha_Salida"] = entry_fecha_salida.get()
                paquete["Hora_Salida"] = entry_hora_salida.get()
                paquete["Fecha_Llegada"] = entry_fecha_llegada.get()
                paquete["Hora_Llegada"] = entry_hora_llegada.get()

                tree.item(selected_item, values=(paquete["ID"], paquete["Cliente"], paquete["Distribuidor"], paquete["Estado"], paquete["Fase"], paquete["Fecha_Salida"], paquete["Hora_Salida"], paquete["Fecha_Llegada"], paquete["Hora_Llegada"]))
                messagebox.showinfo("Éxito", "Fechas y horarios actualizados con éxito")
                root.destroy()

            btn_guardar = tk.Button(root, text="Guardar Cambios", command=guardar_fechas)
            btn_guardar.grid(row=4, column=0, columnspan=2, pady=10)
        else:
            messagebox.showerror("Error", "Paquete no encontrado")
    else:
        messagebox.showerror("Error", "Seleccione un paquete para cambiar fechas y horarios")

def centrar_ventana(ventana, ancho, alto):
    pantalla_width = ventana.winfo_screenwidth()
    pantalla_height = ventana.winfo_screenheight()
    x = (pantalla_width // 2) - (ancho // 2)
    y = (pantalla_height // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")