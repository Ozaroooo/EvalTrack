<<<<<<< HEAD
class Estudiante:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.lista_calificaciones = []

    def agregar_calificacion(self, calificacion):
        if 0 <= calificacion <= 50:
            self.lista_calificaciones.append(calificacion)
        else:
            print("Calificación fuera de rango (0-50).")

    def actualizar_calificacion(self, indice, nueva_calificacion):
        if 0 <= nueva_calificacion <= 50:
            if 0 <= indice < len(self.lista_calificaciones):
                self.lista_calificaciones[indice] = nueva_calificacion
                print("Calificación actualizada correctamente.")
            else:
                print("Índice no válido.")
        else:
            print("Nueva calificación fuera de rango (0-50).")

    def calcular_promedio(self):
        if self.lista_calificaciones:
            return sum(self.lista_calificaciones) / len(self.lista_calificaciones)
        return 0.0

class GestorEstudiantes:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self):
        while True:
            try:
                id = int(input("Ingrese ID del estudiante (mayor a 0): "))
                if id > 0:
                    break
                else:
                    print("El ID debe ser un número mayor a 0.")
            except ValueError:
                print("Entrada inválida. Ingrese un número entero.")

        nombre = input("Ingrese nombre del estudiante: ")
        nuevo_estudiante = Estudiante(id, nombre)
        self.estudiantes.append(nuevo_estudiante)
        print(f"Estudiante {nombre} agregado exitosamente.")

    def ingresar_calificaciones(self):
        id = int(input("Ingrese ID del estudiante: "))
        for estudiante in self.estudiantes:
            if estudiante.id == id:
                while True:
                    try:
                        calificacion = float(input("Ingrese calificación (0-50) o -1 para salir: "))
                        if calificacion == -1:
                            break
                        estudiante.agregar_calificacion(calificacion)
                    except ValueError:
                        print("Entrada inválida. Ingrese un número.")
                return
        print("Estudiante no encontrado.")

    def actualizar_calificaciones(self):
        id = int(input("Ingrese ID del estudiante: "))
        for estudiante in self.estudiantes:
            if estudiante.id == id:
                print(f"Calificaciones actuales de {estudiante.nombre}: {estudiante.lista_calificaciones}")
                try:
                    indice = int(input("Ingrese el índice de la calificación a actualizar (comienza desde 0): "))
                    nueva_calificacion = float(input("Ingrese nueva calificación (0-50): "))
                    estudiante.actualizar_calificacion(indice, nueva_calificacion)
                except ValueError:
                    print("Entrada inválida. Asegúrese de ingresar números válidos.")
                return
        print("Estudiante no encontrado.")

    def consultar_estudiantes(self):
        for estudiante in self.estudiantes:
            print(f"ID: {estudiante.id}, Nombre: {estudiante.nombre}, Promedio: {estudiante.calcular_promedio():.2f}")

    def consultar_estudiante_por_id(self):
        id = int(input("Ingrese ID del estudiante a buscar: "))
        for estudiante in self.estudiantes:
            if estudiante.id == id:
                print(f"\nEstudiante encontrado:")
                print(f"ID: {estudiante.id}")
                print(f"Nombre: {estudiante.nombre}")
                print(f"Calificaciones: {estudiante.lista_calificaciones}")
                print(f"Promedio: {estudiante.calcular_promedio():.2f}")
                return
        print("Estudiante no encontrado.")

    def eliminar_estudiante(self):
        id = int(input("Ingrese ID del estudiante a eliminar: "))
        self.estudiantes = [estudiante for estudiante in self.estudiantes if estudiante.id != id]
        print(f"Estudiante con ID {id} eliminado.")

    def mostrar_ficha_tecnica(self):
        ficha = {
            "Sistema de Gestión de Estudiantes"
            "Equipo: EvalTrack"
            "Desarrolladores: Daniel Gamboa, Maria Rincon, Sebastian Camejo, Luis Valencia"
            "Eslogan: 'Educación con Tecnología'"
        }
        print(ficha)

def menu():
    gestor = GestorEstudiantes()
    while True:
        print("\nMenú:")
        print("1. Agregar estudiante")
        print("2. Ingresar calificación")
        print("3. Actualizar calificación")
        print("4. Consultar todos los estudiantes")
        print("5. Buscar estudiante por ID")
        print("6. Eliminar estudiante")
        print("7. Acerca de")
        print("8. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            gestor.agregar_estudiante()
        elif opcion == "2":
            gestor.ingresar_calificaciones()
        elif opcion == "3":
            gestor.actualizar_calificaciones()
        elif opcion == "4":
            gestor.consultar_estudiantes()
        elif opcion == "5":
            gestor.consultar_estudiante_por_id()
        elif opcion == "6":
            gestor.eliminar_estudiante()
        elif opcion == "7":
            gestor.mostrar_ficha_tecnica()
        elif opcion == "8":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

=======
class Estudiante:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.lista_calificaciones = []

    def agregar_calificacion(self, calificacion):
        if 0 <= calificacion <= 50:
            self.lista_calificaciones.append(calificacion)
        else:
            print("Calificación fuera de rango (0-50).")

    def actualizar_calificacion(self, indice, nueva_calificacion):
        if 0 <= nueva_calificacion <= 50:
            if 0 <= indice < len(self.lista_calificaciones):
                self.lista_calificaciones[indice] = nueva_calificacion
                print("Calificación actualizada correctamente.")
            else:
                print("Índice no válido.")
        else:
            print("Nueva calificación fuera de rango (0-50).")

    def calcular_promedio(self):
        if self.lista_calificaciones:
            return sum(self.lista_calificaciones) / len(self.lista_calificaciones)
        return 0.0

class GestorEstudiantes:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self):
        while True:
            try:
                id = int(input("Ingrese ID del estudiante (mayor a 0): "))
                if id > 0:
                    break
                else:
                    print("El ID debe ser un número mayor a 0.")
            except ValueError:
                print("Entrada inválida. Ingrese un número entero.")

        nombre = input("Ingrese nombre del estudiante: ")
        nuevo_estudiante = Estudiante(id, nombre)
        self.estudiantes.append(nuevo_estudiante)
        print(f"Estudiante {nombre} agregado exitosamente.")

    def ingresar_calificaciones(self):
        id = int(input("Ingrese ID del estudiante: "))
        for estudiante in self.estudiantes:
            if estudiante.id == id:
                while True:
                    try:
                        calificacion = float(input("Ingrese calificación (0-50) o -1 para salir: "))
                        if calificacion == -1:
                            break
                        estudiante.agregar_calificacion(calificacion)
                    except ValueError:
                        print("Entrada inválida. Ingrese un número.")
                return
        print("Estudiante no encontrado.")

    def actualizar_calificaciones(self):
        id = int(input("Ingrese ID del estudiante: "))
        for estudiante in self.estudiantes:
            if estudiante.id == id:
                print(f"Calificaciones actuales de {estudiante.nombre}: {estudiante.lista_calificaciones}")
                try:
                    indice = int(input("Ingrese el índice de la calificación a actualizar (comienza desde 0): "))
                    nueva_calificacion = float(input("Ingrese nueva calificación (0-50): "))
                    estudiante.actualizar_calificacion(indice, nueva_calificacion)
                except ValueError:
                    print("Entrada inválida. Asegúrese de ingresar números válidos.")
                return
        print("Estudiante no encontrado.")

    def consultar_estudiantes(self):
        for estudiante in self.estudiantes:
            print(f"ID: {estudiante.id}, Nombre: {estudiante.nombre}, Promedio: {estudiante.calcular_promedio():.2f}")

    def consultar_estudiante_por_id(self):
        id = int(input("Ingrese ID del estudiante a buscar: "))
        for estudiante in self.estudiantes:
            if estudiante.id == id:
                print(f"\nEstudiante encontrado:")
                print(f"ID: {estudiante.id}")
                print(f"Nombre: {estudiante.nombre}")
                print(f"Calificaciones: {estudiante.lista_calificaciones}")
                print(f"Promedio: {estudiante.calcular_promedio():.2f}")
                return
        print("Estudiante no encontrado.")

    def eliminar_estudiante(self):
        id = int(input("Ingrese ID del estudiante a eliminar: "))
        self.estudiantes = [estudiante for estudiante in self.estudiantes if estudiante.id != id]
        print(f"Estudiante con ID {id} eliminado.")

    def mostrar_ficha_tecnica(self):
        ficha = {
            "Sistema de Gestión de Estudiantes"
            "Equipo: EvalTrack"
            "Desarrolladores: Daniel Gamboa, Maria Rincon, Sebastian Camejo, Luis Valencia"
            "Eslogan: 'Educación con Tecnología'"
        }
        print(ficha)

def menu():
    gestor = GestorEstudiantes()
    while True:
        print("\nMenú:")
        print("1. Agregar estudiante")
        print("2. Ingresar calificación")
        print("3. Actualizar calificación")
        print("4. Consultar todos los estudiantes")
        print("5. Buscar estudiante por ID")
        print("6. Eliminar estudiante")
        print("7. Acerca de")
        print("8. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            gestor.agregar_estudiante()
        elif opcion == "2":
            gestor.ingresar_calificaciones()
        elif opcion == "3":
            gestor.actualizar_calificaciones()
        elif opcion == "4":
            gestor.consultar_estudiantes()
        elif opcion == "5":
            gestor.consultar_estudiante_por_id()
        elif opcion == "6":
            gestor.eliminar_estudiante()
        elif opcion == "7":
            gestor.mostrar_ficha_tecnica()
        elif opcion == "8":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

>>>>>>> d25fdcb057c4e6bd62d8fb923d166d4246d76dcb
menu()