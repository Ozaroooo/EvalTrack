import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
import os
import sys
import json

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
        self.usuario_logueado = False
        self.usuarios = self.cargar_usuarios()
        # Fondo con imagen
        if hasattr(sys, '_MEIPASS'):
            bg_path = os.path.join(sys._MEIPASS, "fondoEvalTrack.jpg")
        else:
            bg_path = os.path.join(os.path.dirname(__file__), "fondoEvalTrack.jpg")
        self.bg_image_original = Image.open(bg_path)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image_original.resize((540, 520)))
        self.background_label = tk.Label(self.root, image=self.bg_photo)
        self.background_label.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.root.bind('<Configure>', self._resize_bg)
        # Encabezado visual
        self.header_frame = tk.Frame(root, bg="#3f51b5", height=60)
        self.header_frame.pack(fill="x")
        tk.Label(self.header_frame, text="Gestión de Estudiantes", font=("Arial", 20, "bold"), bg="#3f51b5", fg="white").pack(pady=10)
        # Nueva barra horizontal para los botones
        self.barra_opciones = tk.Frame(root, bg="#e3eafc")
        self.barra_opciones.pack(fill="x", pady=(10, 0))
        # Botones (se habilitan/deshabilitan según login)
        self.btn_agregar = tk.Button(self.barra_opciones, text="Agregar Estudiante", command=self.agregar_estudiante, bg="#4CAF50", fg="white", font=("Arial", 11), width=18, height=2, relief="groove", state="disabled")
        self.btn_agregar.pack(side="left", padx=5, pady=5)
        self.btn_ingresar_calificaciones = tk.Button(self.barra_opciones, text="Ingresar Calificaciones", command=self.ingresar_calificaciones, bg="#FF9800", fg="white", font=("Arial", 11), width=18, height=2, relief="groove", state="disabled")
        self.btn_ingresar_calificaciones.pack(side="left", padx=5, pady=5)
        self.btn_actualizar = tk.Button(self.barra_opciones, text="Actualizar Calificaciones", command=self.actualizar_calificaciones, bg="#009688", fg="white", font=("Arial", 11), width=18, height=2, relief="groove", state="disabled")
        self.btn_actualizar.pack(side="left", padx=5, pady=5)
        self.btn_consultar = tk.Button(self.barra_opciones, text="Consultar Estudiantes", command=self.consultar_estudiantes, bg="#2196F3", fg="white", font=("Arial", 11), width=18, height=2, relief="groove", state="disabled")
        self.btn_consultar.pack(side="left", padx=5, pady=5)
        self.btn_buscar = tk.Button(self.barra_opciones, text="Buscar Estudiante por ID", command=self.consultar_estudiante_por_id, bg="#9C27B0", fg="white", font=("Arial", 11), width=18, height=2, relief="groove", state="disabled")
        self.btn_buscar.pack(side="left", padx=5, pady=5)
        self.btn_eliminar = tk.Button(self.barra_opciones, text="Eliminar Estudiante", command=self.eliminar_estudiante, bg="#F44336", fg="white", font=("Arial", 11), width=18, height=2, relief="groove", state="disabled")
        self.btn_eliminar.pack(side="left", padx=5, pady=5)
        # Botones de login/register
        self.btn_login = tk.Button(self.barra_opciones, text="Login", command=self.mostrar_login, bg="#607d8b", fg="white", font=("Arial", 11), width=12, height=2, relief="groove")
        self.btn_login.pack(side="right", padx=5, pady=5)
        self.btn_register = tk.Button(self.barra_opciones, text="Registrar", command=self.mostrar_registro, bg="#8bc34a", fg="white", font=("Arial", 11), width=12, height=2, relief="groove")
        self.btn_register.pack(side="right", padx=5, pady=5)
        self.btn_logout = tk.Button(self.barra_opciones, text="Logout", command=self.logout, bg="#b71c1c", fg="white", font=("Arial", 11), width=12, height=2, relief="groove")
        self.btn_logout.pack_forget()  # Oculto por defecto
        # Botón para cambiar tema
        self.btn_tema = tk.Button(self.barra_opciones, text="Cambiar tema", command=self.toggle_tema, bg="#607d8b", fg="white", font=("Arial", 11), width=14, height=2, relief="groove")
        self.btn_tema.pack(side="right", padx=5, pady=5)
        # Botón "Acerca de"
        self.btn_acerca = tk.Button(self.barra_opciones, text="Acerca de", command=self.mostrar_acerca_de, bg="#607d8b", fg="white", font=("Arial", 11), width=14, height=2, relief="groove")
        self.btn_acerca.pack(side="right", padx=5, pady=5)
        # Contenedor principal para mostrar vistas dinámicas
        self.main_frame = tk.Frame(self.root, bg="#f5f5f5")
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=(80, 10))
        # Sección "Acerca de" como texto fijo en la interfaz debajo de los botones
        # self.label_acerca = tk.Label(root, text="Sistema de Gestión de Estudiantes\n"
        #                                 "Equipo: EvalTrack\n"
        #                                 "Desarrolladores: Daniel Gamboa, Maria Rincon, Sebastian Camejo, Luis Valencia\n"
        #                                 " 'Educación con Tecnología'", 
        #                                 font=("Arial", 10, "italic"), bg="#e3eafc", fg="gray")
        # self.label_acerca.pack(side="bottom", pady=10)
        self.cargar_desde_archivo()
        self.mostrar_login()

    def cargar_usuarios(self):
        try:
            with open("usuarios.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def guardar_usuarios(self):
        with open("usuarios.json", "w", encoding="utf-8") as f:
            json.dump(self.usuarios, f, ensure_ascii=False, indent=2)

    def mostrar_registro(self):
        self.limpiar_main_frame()
        ventana = self.main_frame
        ventana.configure(bg="#f5f5f5")
        tk.Label(ventana, text="Registro de Usuario", font=("Arial", 14, "bold"), bg="#f5f5f5").pack(pady=10)
        tk.Label(ventana, text="Usuario:", font=("Arial", 11), bg="#f5f5f5").pack()
        usuario_entry = tk.Entry(ventana, font=("Arial", 11))
        usuario_entry.pack()
        tk.Label(ventana, text="Contraseña:", font=("Arial", 11), bg="#f5f5f5").pack()
        password_entry = tk.Entry(ventana, font=("Arial", 11), show="*")
        password_entry.pack()
        def registrar():
            usuario = usuario_entry.get()
            password = password_entry.get()
            if not usuario or not password:
                messagebox.showerror("Error", "Debe ingresar usuario y contraseña.")
                return
            if usuario in self.usuarios:
                messagebox.showerror("Error", "El usuario ya existe.")
                return
            self.usuarios[usuario] = password
            self.guardar_usuarios()
            messagebox.showinfo("Éxito", "Usuario registrado correctamente. Ahora puede iniciar sesión.")
            self.mostrar_login()
        tk.Button(ventana, text="Registrar", command=registrar, bg="#8bc34a", fg="white", font=("Arial", 11), width=12).pack(pady=10)

    def mostrar_login(self):
        self.limpiar_main_frame()
        ventana = self.main_frame
        ventana.configure(bg="#f5f5f5")
        tk.Label(ventana, text="Iniciar Sesión", font=("Arial", 14, "bold"), bg="#f5f5f5").pack(pady=10)
        tk.Label(ventana, text="Usuario:", font=("Arial", 11), bg="#f5f5f5").pack()
        usuario_entry = tk.Entry(ventana, font=("Arial", 11))
        usuario_entry.pack()
        tk.Label(ventana, text="Contraseña:", font=("Arial", 11), bg="#f5f5f5").pack()
        password_entry = tk.Entry(ventana, font=("Arial", 11), show="*")
        password_entry.pack()
        def login():
            usuario = usuario_entry.get()
            password = password_entry.get()
            if usuario in self.usuarios and self.usuarios[usuario] == password:
                self.usuario_logueado = True
                self.habilitar_opciones(True)
                self.btn_login.pack_forget()
                self.btn_register.pack_forget()
                self.btn_logout.pack(side="right", padx=5, pady=5)
                messagebox.showinfo("Bienvenido", f"Bienvenido, {usuario}!")
                self.limpiar_main_frame()
            else:
                messagebox.showerror("Error", "Usuario o contraseña incorrectos.")
        tk.Button(ventana, text="Iniciar Sesión", command=login, bg="#607d8b", fg="white", font=("Arial", 11), width=12).pack(pady=10)
        def mostrar_reestablecer():
            self.limpiar_main_frame()
            ventana = self.main_frame
            ventana.configure(bg="#f5f5f5")
            tk.Label(ventana, text="Reestablecer contraseña", font=("Arial", 14, "bold"), bg="#f5f5f5").pack(pady=10)
            tk.Label(ventana, text="Usuario:", font=("Arial", 11), bg="#f5f5f5").pack()
            usuario_entry2 = tk.Entry(ventana, font=("Arial", 11))
            usuario_entry2.pack()
            tk.Label(ventana, text="Nueva contraseña:", font=("Arial", 11), bg="#f5f5f5").pack()
            nueva_entry = tk.Entry(ventana, font=("Arial", 11), show="*")
            nueva_entry.pack()
            def reestablecer():
                usuario = usuario_entry2.get()
                nueva = nueva_entry.get()
                if not usuario or not nueva:
                    messagebox.showerror("Error", "Debe ingresar usuario y nueva contraseña.")
                    return
                if usuario not in self.usuarios:
                    messagebox.showerror("Error", "El usuario no existe.")
                    return
                self.usuarios[usuario] = nueva
                self.guardar_usuarios()
                messagebox.showinfo("Éxito", "Contraseña reestablecida correctamente. Ahora puede iniciar sesión.")
                self.mostrar_login()
            tk.Button(ventana, text="Reestablecer", command=reestablecer, bg="#607d8b", fg="white", font=("Arial", 11), width=12).pack(pady=10)
            tk.Button(ventana, text="Volver", command=self.mostrar_login, bg="#bdbdbd", fg="#333", font=("Arial", 10), relief="flat").pack(pady=2)
        tk.Button(ventana, text="¿Olvidó su contraseña?", command=mostrar_reestablecer, bg="#bdbdbd", fg="#333", font=("Arial", 10, "italic"), relief="flat").pack(pady=2)

    def logout(self):
        self.usuario_logueado = False
        self.habilitar_opciones(False)
        self.btn_logout.pack_forget()
        self.btn_login.pack(side="right", padx=5, pady=5)
        self.btn_register.pack(side="right", padx=5, pady=5)
        self.limpiar_main_frame()
        self.mostrar_login()

    def habilitar_opciones(self, habilitar):
        estado = "normal" if habilitar else "disabled"
        self.btn_agregar.config(state=estado)
        self.btn_ingresar_calificaciones.config(state=estado)
        self.btn_actualizar.config(state=estado)
        self.btn_consultar.config(state=estado)
        self.btn_buscar.config(state=estado)
        self.btn_eliminar.config(state=estado)

    def limpiar_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def crear_tabla(self):
        pass  # Ya no se usa base de datos

    def cargar_estudiantes(self):
        pass  # Ya no se usa base de datos

    def guardar_en_archivo(self):
        datos = [
            {
                "id": est.id,
                "nombre": est.nombre,
                "cedula": est.cedula,
                "calificaciones": est.calificaciones
            }
            for est in self.estudiantes
        ]
        with open("estudiantes.json", "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=2)

    def cargar_desde_archivo(self):
        try:
            with open("estudiantes.json", "r", encoding="utf-8") as f:
                datos = json.load(f)
            self.estudiantes = [
                Estudiante(d["id"], d["nombre"], d["cedula"])
                for d in datos
            ]
            for est, d in zip(self.estudiantes, datos):
                est.calificaciones = d.get("calificaciones", [])
        except FileNotFoundError:
            self.estudiantes = []

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
                # Ordenar la lista de estudiantes por ID numérico
                try:
                    self.estudiantes.sort(key=lambda e: int(e.id))
                except ValueError:
                    self.estudiantes.sort(key=lambda e: e.id)  # Si algún ID no es numérico, ordena como texto
                self.guardar_en_archivo()
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
            # Validación estricta de rango 0-50
            for cal in calificaciones:
                if cal < 0 or cal > 50:
                    messagebox.showerror("Error", "Las calificaciones deben estar entre 0 y 50.")
                    return
            for cal in calificaciones:
                estudiante.agregar_calificacion(cal)
            self.guardar_en_archivo()
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
            self.guardar_en_archivo()
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
                self.guardar_en_archivo()
                messagebox.showinfo("Éxito", "Estudiante eliminado correctamente.")
                self.limpiar_main_frame()
            else:
                messagebox.showerror("Error", "Estudiante no encontrado.")

        tk.Button(ventana, text="Eliminar", command=eliminar, bg="#F44336", fg="white", font=("Arial", 11), width=12).pack(pady=10)

    def mostrar_acerca_de(self):
        self.limpiar_main_frame()
        ventana = self.main_frame
        ventana.configure(bg="#f5f5f5")
        acerca_texto = (
            "Sistema de Gestión de Estudiantes\n"
            "Equipo: EvalTrack\n"
            "Desarrolladores: Daniel Gamboa, Maria Rincon, Sebastian Camejo, Luis Valencia\n"
            "'Educación con Tecnología'"
        )
        tk.Label(ventana, text="Acerca de", font=("Arial", 16, "bold"), bg="#f5f5f5", fg="#3f51b5").pack(pady=(30,10))
        tk.Label(ventana, text=acerca_texto, font=("Arial", 12, "italic"), bg="#f5f5f5", fg="#333").pack(pady=10)
        tk.Button(ventana, text="Volver", command=self.limpiar_main_frame, bg="#607d8b", fg="white", font=("Arial", 11), width=12).pack(pady=20)

    def toggle_tema(self):
        # Alterna entre tema claro y oscuro
        if not hasattr(self, 'tema_oscuro'):
            self.tema_oscuro = False
        self.tema_oscuro = not self.tema_oscuro
        if self.tema_oscuro:
            # Tema oscuro
            bg_main = "#23272e"
            bg_frame = "#23272e"
            fg_text = "#f5f5f5"
            btn_bg = "#444c56"
            btn_fg = "#f5f5f5"
            header_bg = "#11151a"
        else:
            # Tema claro (original)
            bg_main = "#e3eafc"
            bg_frame = "#f5f5f5"
            fg_text = "#222"
            btn_bg = "#4CAF50"
            btn_fg = "white"
            header_bg = "#3f51b5"
        self.root.configure(bg=bg_main)
        self.main_frame.configure(bg=bg_frame)
        self.barra_opciones.configure(bg=bg_main)
        for btn in [self.btn_agregar, self.btn_ingresar_calificaciones, self.btn_actualizar, self.btn_consultar, self.btn_buscar, self.btn_eliminar]:
            btn.configure(bg=btn_bg, fg=btn_fg)
        self.btn_login.configure(bg=btn_bg, fg=btn_fg)
        self.btn_register.configure(bg=btn_bg, fg=btn_fg)
        self.btn_logout.configure(bg="#b71c1c" if not self.tema_oscuro else "#a93226", fg=btn_fg)
        self.header_frame.configure(bg=header_bg)
        self.limpiar_main_frame()  # Solo esta llamada, NO llames a self.animar_fade_in_main_frame() aquí

    def animar_fade_in_main_frame(self, steps=12, delay=20):
        # Animación de fade in para el main_frame
        if self.tema_oscuro:
            start = 35  # más oscuro
            end = 35 + 30  # un poco más claro
        else:
            start = 245
            end = 245 - 30  # un poco más oscuro
        diff = (end - start) / steps
        def fade(step=0):
            val = int(start + diff * step)
            color = f"#{val:02x}{val:02x}{val:02x}"
            self.main_frame.configure(bg=color)
            for w in self.main_frame.winfo_children():
                try:
                    w.configure(bg=color)
                except:
                    pass
            if step < steps:
                self.root.after(delay, lambda: fade(step+1))
            else:
                # Restaurar color final según tema
                final = "#23272e" if self.tema_oscuro else "#f5f5f5"
                self.main_frame.configure(bg=final)
                for w in self.main_frame.winfo_children():
                    try:
                        w.configure(bg=final)
                    except:
                        pass
        fade()

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