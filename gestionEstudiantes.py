import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
import os
import sys

# Clase que representa a un estudiante con su ID, nombre y lista de calificaciones
class Estudiante:
    def __init__(self, id, nombre, cedula):
        # Constructor: inicializa el ID, nombre, cédula y lista vacía de calificaciones
        self.id = id
        self.nombre = nombre
        self.cedula = cedula
        self.calificaciones = []

    def agregar_calificacion(self, calificacion):
        # Agrega una calificación si está en el rango permitido (0-50)
        if 0 <= calificacion <= 50:
            self.calificaciones.append(calificacion)
        else:
            print("Calificación fuera de rango (0-50).")

    def actualizar_calificacion(self, indice, nueva_calificacion):
        # Permite actualizar una calificación existente por su índice
        if 0 <= nueva_calificacion <= 50:
            if 0 <= indice < len(self.calificaciones):
                self.calificaciones[indice] = nueva_calificacion
            else:
                print("Índice de calificación inválido.")
        else:
            print("Nueva calificación fuera de rango (0-50).")

    def calcular_promedio(self):
        # Calcula el promedio de las calificaciones del estudiante
        return sum(self.calificaciones) / len(self.calificaciones) if self.calificaciones else 0.0


# Clase que gestiona la lista de estudiantes y las operaciones sobre ellos
class GestorEstudiantesGUI:
    def __init__(self, root):
        self.estudiantes = []
        self.root = root
        self.root.title("Sistema de Gestión de Estudiantes")
        self.root.geometry("540x520")
        self.root.configure(bg="#e3eafc")
        # Fondo con imagen
        bg_path = os.path.join(os.path.dirname(__file__), "fondoEvalTrack.jpg")
        self.bg_image_original = Image.open(bg_path)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image_original.resize((540, 520)))
        self.background_label = tk.Label(self.root, image=self.bg_photo)
        self.background_label.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.root.bind('<Configure>', self._resize_bg)
        # Encabezado visual
        header_frame = tk.Frame(root, bg="#3f51b5", height=60)
        header_frame.pack(fill="x")
        tk.Label(header_frame, text="Gestión de Estudiantes", font=("Arial", 20, "bold"), bg="#3f51b5", fg="white").pack(pady=10)

        # Nueva barra horizontal para los botones
        barra_opciones = tk.Frame(root, bg="#e3eafc")
        barra_opciones.pack(fill="x", pady=(10, 0))

        self.btn_agregar = tk.Button(barra_opciones, text="Agregar Estudiante", command=self.agregar_estudiante, bg="#4CAF50", fg="white", font=("Arial", 11), width=18, height=2, relief="groove")
        self.btn_agregar.pack(side="left", padx=5, pady=5)

        self.btn_ingresar_calificaciones = tk.Button(barra_opciones, text="Ingresar Calificaciones", command=self.ingresar_calificaciones, bg="#FF9800", fg="white", font=("Arial", 11), width=18, height=2, relief="groove")
        self.btn_ingresar_calificaciones.pack(side="left", padx=5, pady=5)

        self.btn_actualizar = tk.Button(barra_opciones, text="Actualizar Calificaciones", command=self.actualizar_calificaciones, bg="#009688", fg="white", font=("Arial", 11), width=18, height=2, relief="groove")
        self.btn_actualizar.pack(side="left", padx=5, pady=5)

        self.btn_consultar = tk.Button(barra_opciones, text="Consultar Estudiantes", command=self.consultar_estudiantes, bg="#2196F3", fg="white", font=("Arial", 11), width=18, height=2, relief="groove")
        self.btn_consultar.pack(side="left", padx=5, pady=5)

        self.btn_buscar = tk.Button(barra_opciones, text="Buscar Estudiante por ID", command=self.consultar_estudiante_por_id, bg="#9C27B0", fg="white", font=("Arial", 11), width=18, height=2, relief="groove")
        self.btn_buscar.pack(side="left", padx=5, pady=5)

        self.btn_eliminar = tk.Button(barra_opciones, text="Eliminar Estudiante", command=self.eliminar_estudiante, bg="#F44336", fg="white", font=("Arial", 11), width=18, height=2, relief="groove")
        self.btn_eliminar.pack(side="left", padx=5, pady=5)

        # Contenedor principal para mostrar vistas dinámicas
        self.main_frame = tk.Frame(self.root, bg="#f5f5f5")
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=(80, 10))

        # Sección "Acerca de" como texto fijo en la interfaz debajo de los botones
        self.label_acerca = tk.Label(root, text="Sistema de Gestión de Estudiantes\n"
                                        "Equipo: EvalTrack\n"
                                        "Desarrolladores: Daniel Gamboa, Maria Rincon, Sebastian Camejo, Luis Valencia\n"
                                        "Eslogan: 'Educación con Tecnología'", 
                                        font=("Arial", 10, "italic"), bg="#e3eafc", fg="gray")
        self.label_acerca.pack(side="bottom", pady=10)

    def limpiar_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def crear_tabla(self):
        pass  # Ya no se usa base de datos

    def cargar_estudiantes(self):
        pass  # Ya no se usa base de datos

    def guardar_en_db(self, estudiante):
        pass  # Ya no se usa base de datos

    def eliminar_de_db(self, id):
        pass  # Ya no se usa base de datos

    def agregar_estudiante(self):
        self.limpiar_main_frame()
        ventana = self.main_frame
        ventana.configure(bg="#f5f5f5")
        tk.Label(ventana, text="ID:", font=("Arial", 11), bg="#f5f5f5").pack(pady=(15,2))
        id_entry = tk.Entry(ventana, font=("Arial", 11))
        id_entry.pack(pady=2)

        tk.Label(ventana, text="Nombre:", font=("Arial", 11), bg="#f5f5f5").pack(pady=2)
        nombre_entry = tk.Entry(ventana, font=("Arial", 11))
        nombre_entry.pack(pady=2)

        tk.Label(ventana, text="Cédula:", font=("Arial", 11), bg="#f5f5f5").pack(pady=2)
        cedula_entry = tk.Entry(ventana, font=("Arial", 11))
        cedula_entry.pack(pady=2)

        def guardar():
            id = id_entry.get()
            nombre = nombre_entry.get()
            cedula = cedula_entry.get()
            # Verificar si el ID ya existe
            if any(est.id == id for est in self.estudiantes):
                messagebox.showerror("Error", "Ya existe un estudiante con ese ID.")
                return
            if id and nombre and cedula:
                estudiante = Estudiante(id, nombre, cedula)
                self.estudiantes.append(estudiante)
                self.guardar_en_db(estudiante)
                messagebox.showinfo("Éxito", "Estudiante agregado correctamente.")
                self.limpiar_main_frame()
            else:
                messagebox.showerror("Error", "Debe ingresar todos los datos.")

        tk.Button(ventana, text="Guardar", command=guardar, bg="#4CAF50", fg="white", font=("Arial", 11), width=12).pack(pady=10)

    def ingresar_calificaciones(self):
        self.limpiar_main_frame()
        ventana = self.main_frame
        ventana.configure(bg="#f5f5f5")
        tk.Label(ventana, text="ID del Estudiante:", font=("Arial", 11), bg="#f5f5f5").pack(pady=(15,2))
        id_entry = tk.Entry(ventana, font=("Arial", 11))
        id_entry.pack(pady=2)

        tk.Label(ventana, text="Cantidad de calificaciones:", font=("Arial", 11), bg="#f5f5f5").pack(pady=2)
        cantidad_entry = tk.Entry(ventana, font=("Arial", 11))
        cantidad_entry.pack(pady=2)

        calificacion_entries = []
        calificaciones_frame = tk.Frame(ventana, bg="#f5f5f5")
        calificaciones_frame.pack(pady=5)

        def mostrar_campos():
            for widget in calificaciones_frame.winfo_children():
                widget.destroy()
            calificacion_entries.clear()
            id = id_entry.get()
            estudiante = next((e for e in self.estudiantes if e.id == id), None)
            if not estudiante:
                messagebox.showerror("Error", "No existe este id de estudiante.")
                return
            try:
                cantidad = int(cantidad_entry.get())
                if cantidad <= 0:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Error", "Ingrese una cantidad válida.")
                return
            for i in range(cantidad):
                tk.Label(calificaciones_frame, text=f"Calificación {i+1} (0-50):", font=("Arial", 10), bg="#f5f5f5").pack()
                entry = tk.Entry(calificaciones_frame, font=("Arial", 10))
                entry.pack()
                calificacion_entries.append(entry)

        def guardar():
            id = id_entry.get()
            estudiante = next((e for e in self.estudiantes if e.id == id), None)
            if not estudiante:
                messagebox.showerror("Error", "No existe este id de estudiante.")
                return
            try:
                calificaciones = [float(e.get()) for e in calificacion_entries]
            except ValueError:
                messagebox.showerror("Error", "Ingrese solo números válidos.")
                return
            for cal in calificaciones:
                estudiante.agregar_calificacion(cal)
            self.guardar_en_db(estudiante)
            messagebox.showinfo("Éxito", "Calificaciones agregadas correctamente.")
            self.limpiar_main_frame()
        tk.Button(ventana, text="Aceptar cantidad", command=mostrar_campos, bg="#2196F3", fg="white", font=("Arial", 10), width=16).pack(pady=5)
        tk.Button(ventana, text="Guardar", command=guardar, bg="#FF9800", fg="white", font=("Arial", 11), width=12).pack(pady=10)

    def actualizar_calificaciones(self):
        self.limpiar_main_frame()
        ventana = self.main_frame
        ventana.configure(bg="#f5f5f5")
        tk.Label(ventana, text="ID del Estudiante:", font=("Arial", 11), bg="#f5f5f5").pack(pady=(15,2))
        id_entry = tk.Entry(ventana, font=("Arial", 11))
        id_entry.pack(pady=2)

        result_label = tk.Label(ventana, text="", font=("Arial", 10), bg="#f5f5f5")
        result_label.pack(pady=5)

        calificacion_entries = []
        calificaciones_frame = tk.Frame(ventana, bg="#f5f5f5")
        calificaciones_frame.pack(pady=5)

        def buscar():
            for widget in calificaciones_frame.winfo_children():
                widget.destroy()
            calificacion_entries.clear()
            id = id_entry.get()
            estudiante = next((e for e in self.estudiantes if e.id == id), None)
            if estudiante and estudiante.calificaciones:
                result_label.config(text=f"Calificaciones actuales: {estudiante.calificaciones}", fg="#333")
                for i, cal in enumerate(estudiante.calificaciones):
                    tk.Label(calificaciones_frame, text=f"Índice {i}:", font=("Arial", 10), bg="#f5f5f5").pack()
                    entry = tk.Entry(calificaciones_frame, font=("Arial", 10))
                    entry.insert(0, str(cal))
                    entry.pack()
                    calificacion_entries.append(entry)
            elif estudiante:
                result_label.config(text="El estudiante no tiene calificaciones registradas.", fg="red")
            else:
                result_label.config(text="Estudiante no encontrado.", fg="red")

        def guardar():
            id = id_entry.get()
            estudiante = next((e for e in self.estudiantes if e.id == id), None)
            if not estudiante:
                messagebox.showerror("Error", "Estudiante no encontrado.")
                return
            try:
                nuevas = [float(e.get()) for e in calificacion_entries]
            except ValueError:
                messagebox.showerror("Error", "Ingrese solo números válidos.")
                return
            for i, nueva in enumerate(nuevas):
                estudiante.actualizar_calificacion(i, nueva)
            self.guardar_en_db(estudiante)
            messagebox.showinfo("Éxito", "Calificaciones actualizadas correctamente.")
            self.limpiar_main_frame()

        tk.Button(ventana, text="Buscar", command=buscar, bg="#009688", fg="white", font=("Arial", 10), width=16).pack(pady=5)
        tk.Button(ventana, text="Guardar", command=guardar, bg="#009688", fg="white", font=("Arial", 11), width=12).pack(pady=10)

    def consultar_estudiantes(self):
        self.limpiar_main_frame()
        ventana = self.main_frame
        ventana.configure(bg="#f5f5f5")
        frame = tk.Frame(ventana, bg="#f5f5f5")
        frame.pack(fill="both", expand=True, padx=10, pady=10)
        canvas = tk.Canvas(frame, bg="#f5f5f5", highlightthickness=0)
        scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg="#f5f5f5")
        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Encabezados estilo Excel
        headers = ["ID", "Nombre", "Cédula", "Promedio"]
        for col, header in enumerate(headers):
            tk.Label(scroll_frame, text=header, font=("Arial", 11, "bold"), bg="#c5cae9", fg="#222", borderwidth=1, relief="solid", width=18).grid(row=0, column=col, sticky="nsew", padx=1, pady=1)

        for row, estudiante in enumerate(self.estudiantes, start=1):
            tk.Label(scroll_frame, text=estudiante.id, font=("Arial", 11), bg="#f5f5f5", borderwidth=1, relief="solid", width=18).grid(row=row, column=0, sticky="nsew", padx=1, pady=1)
            tk.Label(scroll_frame, text=estudiante.nombre, font=("Arial", 11), bg="#f5f5f5", borderwidth=1, relief="solid", width=18).grid(row=row, column=1, sticky="nsew", padx=1, pady=1)
            tk.Label(scroll_frame, text=estudiante.cedula, font=("Arial", 11), bg="#f5f5f5", borderwidth=1, relief="solid", width=18).grid(row=row, column=2, sticky="nsew", padx=1, pady=1)
            tk.Label(scroll_frame, text=f"{estudiante.calcular_promedio():.2f}", font=("Arial", 11), bg="#f5f5f5", borderwidth=1, relief="solid", width=18).grid(row=row, column=3, sticky="nsew", padx=1, pady=1)

        # Ajustar columnas para que se expandan
        for col in range(4):
            scroll_frame.grid_columnconfigure(col, weight=1)

    def consultar_estudiante_por_id(self):
        self.limpiar_main_frame()
        ventana = self.main_frame
        ventana.configure(bg="#f5f5f5")
        tk.Label(ventana, text="ID del Estudiante:", font=("Arial", 11), bg="#f5f5f5").pack(pady=(15,2))
        id_entry = tk.Entry(ventana, font=("Arial", 11))
        id_entry.pack(pady=2)

        result_label = tk.Label(ventana, text="", font=("Arial", 11), bg="#f5f5f5")
        result_label.pack(pady=10)

        def buscar():
            id = id_entry.get()
            estudiante = next((e for e in self.estudiantes if e.id == id), None)
            if estudiante:
                result_label.config(text=f"Nombre: {estudiante.nombre}\nCédula: {estudiante.cedula}\nPromedio: {estudiante.calcular_promedio():.2f}", fg="#333")
            else:
                result_label.config(text="Estudiante no encontrado.", fg="red")

        tk.Button(ventana, text="Buscar", command=buscar, bg="#9C27B0", fg="white", font=("Arial", 11), width=12).pack(pady=5)

    def eliminar_estudiante(self):
        self.limpiar_main_frame()
        ventana = self.main_frame
        ventana.configure(bg="#f5f5f5")
        tk.Label(ventana, text="ID del Estudiante a Eliminar:", font=("Arial", 11), bg="#f5f5f5").pack(pady=(20,2))
        id_entry = tk.Entry(ventana, font=("Arial", 11))
        id_entry.pack(pady=2)

        def eliminar():
            id = id_entry.get()
            if any(est.id == id for est in self.estudiantes):
                self.estudiantes = [est for est in self.estudiantes if est.id != id]
                self.eliminar_de_db(id)
                messagebox.showinfo("Éxito", "Estudiante eliminado correctamente.")
                self.limpiar_main_frame()
            else:
                messagebox.showerror("Error", "Estudiante no encontrado.")

        tk.Button(ventana, text="Eliminar", command=eliminar, bg="#F44336", fg="white", font=("Arial", 11), width=12).pack(pady=10)

    def _resize_bg(self, event):
        # Redimensiona el fondo al cambiar el tamaño de la ventana
        if event.widget == self.root:
            new_width = max(1, event.width)
            new_height = max(1, event.height)
            resized = self.bg_image_original.resize((new_width, new_height), Image.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(resized)
            self.background_label.config(image=self.bg_photo)
            self.background_label.image = self.bg_photo

    def __del__(self):
        pass  # Ya no se usa base de datos

# Ejecutar la aplicación gráfica
if __name__ == "__main__":
    root = tk.Tk()
    app = GestorEstudiantesGUI(root)
    root.mainloop()