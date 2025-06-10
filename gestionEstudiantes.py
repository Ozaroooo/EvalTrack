# Clase que representa a un estudiante con su ID, nombre y lista de calificaciones
class Estudiante:
    def __init__(self, id, nombre):
        # Constructor: inicializa el ID, nombre y lista vacía de calificaciones
        self.id = id
        self.nombre = nombre
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
class GestorEstudiantes:
    def __init__(self):
        # Constructor: inicializa la lista vacía de estudiantes
        self.estudiantes = []

    def agregar_estudiante(self):
        # Solicita datos por consola y agrega un nuevo estudiante a la lista
        id = input("Ingrese el ID del estudiante: ")
        nombre = input("Ingrese el nombre del estudiante: ")
        self.estudiantes.append(Estudiante(id, nombre))

    def ingresar_calificaciones(self):
        # Permite ingresar varias calificaciones a un estudiante existente
        id = input("Ingrese el ID del estudiante: ")
        estudiante = next((e for e in self.estudiantes if e.id == id), None)
        if estudiante:
            while True:
                try:
                    calificacion = float(input("Ingrese la calificación (0-50) o -1 para salir: "))
                    if calificacion == -1:
                        break
                    estudiante.agregar_calificacion(calificacion)
                except ValueError:
                    print("Entrada inválida, ingrese un número.")
        else:
            print("Estudiante no encontrado.")

    def actualizar_calificaciones(self):
        # Permite modificar una calificación específica de un estudiante
        id = input("Ingrese el ID del estudiante: ")
        estudiante = next((e for e in self.estudiantes if e.id == id), None)
        if estudiante:
            if estudiante.calificaciones:
                print(f"Calificaciones actuales de {estudiante.nombre}: {estudiante.calificaciones}")
                try:
                    indice = int(input("Ingrese el índice de la calificación que desea modificar (empezando desde 0): "))
                    nueva_calificacion = float(input("Ingrese la nueva calificación (0-50): "))
                    estudiante.actualizar_calificacion(indice, nueva_calificacion)
                except ValueError:
                    print("Entrada inválida, ingrese un número válido.")
            else:
                print("El estudiante no tiene calificaciones registradas.")
        else:
            print("Estudiante no encontrado.")

    def consultar_estudiantes(self):
        # Muestra todos los estudiantes y su promedio de calificaciones
        for estudiante in self.estudiantes:
            print(f"ID: {estudiante.id}, Nombre: {estudiante.nombre}, Promedio: {estudiante.calcular_promedio():.2f}")

    def consultar_estudiante_por_id(self):
        # Busca y muestra la información de un estudiante por su ID
        id = input("Ingrese el ID del estudiante que desea buscar: ")
        estudiante = next((e for e in self.estudiantes if e.id == id), None)
        if estudiante:
            print(f"ID: {estudiante.id}, Nombre: {estudiante.nombre}, Promedio: {estudiante.calcular_promedio():.2f}")
        else:
            print("Estudiante no encontrado.")

    def eliminar_estudiante(self):
        # Elimina un estudiante de la lista por su ID
        id = input("Ingrese el ID del estudiante a eliminar: ")
        self.estudiantes = [est for est in self.estudiantes if est.id != id]

    def mostrar_ficha_tecnica(self):
        # Muestra información del sistema y del equipo desarrollador
        print("Sistema de Gestión de Estudiantes")
        print("Equipo: EvalTrack")
        print("Desarrolladores: Daniel Gamboa, Maria Rincon, Sebastian Camejo, Luis Valencia")
        print("Eslogan: 'Educación con Tecnología'")


# Función principal que muestra el menú y gestiona la interacción con el usuario
# Se utiliza un bucle para mostrar las opciones y ejecutar la acción seleccionada
# El usuario puede agregar, consultar, modificar o eliminar estudiantes, así como ver información del sistema

def mostrar_menu():
    gestor = GestorEstudiantes()
    while True:
        print("\nMenú de opciones:")
        print("1. Agregar estudiante")
        print("2. Ingresar calificaciones")
        print("3. Actualizar calificaciones")
        print("4. Consultar estudiantes y promedios")
        print("5. Consultar un estudiante por ID")
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
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida, intente nuevamente.")


# Ejecutar el programa principal
mostrar_menu()