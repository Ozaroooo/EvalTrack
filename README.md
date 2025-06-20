
# EvalTrack

**EvalTrack** es una aplicación de escritorio desarrollada para facilitar el trabajo de profesores universitarios en el manejo de calificaciones y seguimiento académico de sus estudiantes.

## 📌 Propósito del proyecto

EvalTrack nace como una solución práctica para docentes que necesitan registrar, organizar y consultar las notas de sus estudiantes de manera sencilla, rápida y eficiente, sin depender de hojas de cálculo complejas o plataformas externas.

## 🧩 Características principales

- Registro de estudiantes por curso o materia.
- Ingreso de calificaciones por actividades o parciales.
- Cálculo automático de promedios.
- Visualización clara del rendimiento por estudiante.
- Exportación o respaldo de la información almacenada (opcional, si aplica).
- Interfaz amigable y fácil de usar.

## 📥 Cómo descargar EvalTrack

Puedes descargar la última versión de EvalTrack directamente desde GitHub:

   👉 [Descargar EvalTrack (versión v1.0.0)](https://github.com/Ozaroooo/EvalTrack/releases/download/v1.0.0/EvalTrack.exe)

> 🔒 Recomendamos mover el archivo `EvalTrack.exe` a una carpeta dedicada antes de ejecutarlo, ya que se generarán archivos `.json` que almacenan datos importantes del usuario.

### ⚠️ Advertencia de Windows SmartScreen

Al ejecutar EvalTrack por primera vez, es posible que Windows muestre una advertencia como la siguiente:

![windows_Warn](https://github.com/user-attachments/assets/55576d1c-7ff7-4526-b251-c27ee80d5b27)


Esto sucede porque el archivo no está firmado digitalmente. Para continuar:

1. Haz clic en **"Más información"**.
2. Luego haz clic en **"Ejecutar de todas formas"**.

Aquí puedes ver cómo se ve la segunda pantalla:

![masinformacion_warn](https://github.com/user-attachments/assets/685f40f3-8ba4-4282-a7c5-e47af1f959f8)


## 🖥️ Requisitos del sistema

- Sistema operativo: Windows 10 o superior.
- No requiere instalación: el archivo `EvalTrack.exe` puede ejecutarse directamente.
- (Opcional) Es recomendable tener permisos de escritura en la carpeta donde se ejecuta para guardar los datos correctamente.

## 🚀 Cómo usar EvalTrack

1. Abre `EvalTrack.exe`.
2. Registrarte en la aplicacion colocando un usuario y contraseña.
3. Inicia sesion con los mismos datos con los que te registraste.
4. Crea tus grupos o materias e ingresa los nombres de tus estudiantes.
5. Registra las calificaciones por actividad o evaluación.
6. Consulta los promedios automáticos y haz seguimiento del rendimiento académico.

## 🧱 Estructura del código (Clases principales)

A continuación se describen brevemente las clases clave utilizadas en la aplicación:

### 📄 Clase `Estudiante`

- **Atributos:**
  - `nombre`: nombre completo del estudiante.
  - `notas`: lista de calificaciones.
- **Métodos:**
  - `agregar_nota(nota)`: añade una nueva calificación.
  - `calcular_promedio()`: retorna el promedio de las notas.

### 📄 Clase `Materia`

- **Atributos:**
  - `nombre`: nombre de la materia o curso.
  - `estudiantes`: lista de objetos tipo `Estudiante`.
- **Métodos:**
  - `agregar_estudiante(estudiante)`: agrega un nuevo estudiante.
  - `obtener_promedios()`: devuelve un resumen de promedios por estudiante.

### 📄 Clase `EvalTrackApp`

- **Atributos:**
  - `materias`: lista de materias creadas por el usuario.
- **Métodos:**
  - `crear_materia(nombre)`: instancia una nueva materia.
  - `guardar_datos() / cargar_datos()`: métodos para manejo de archivos JSON.
    
## 🧪 Tecnologías utilizadas

EvalTrack fue desarrollado utilizando las siguientes tecnologías:

- **Python** – como lenguaje principal de programación.
- **Tkinter** – para la interfaz gráfica de usuario (GUI).
- **JSON** – para el almacenamiento local de los datos de estudiantes y calificaciones.
- **OS / datetime** – módulos estándar de Python para gestión de archivos y fechas.

Estas tecnologías permiten que la aplicación sea ligera, portable y fácil de ejecutar sin instalación adicional.


## 👨‍🏫 Público objetivo

Este programa está dirigido a **docentes universitarios** que desean una herramienta rápida y funcional para la gestión de calificaciones sin complicaciones.

## 👥 Desarrolladores

Este proyecto fue desarrollado por:

- **Luis Valencia**
- **Daniel Gamboa**
- **María Rincón**
- **Sebastián Camejo**

## 📂 Estado del proyecto

EvalTrack se encuentra en una versión funcional básica. Se planea incluir futuras mejoras como gráficos de desempeño, generación de reportes PDF y sincronización en la nube.

## 🤝 Contribuciones

Este es un proyecto de uso académico. Si deseas sugerir mejoras, no dudes en compartir tus ideas o comunicarte con el equipo desarrollador.

### 📌 Cómo enviar un Pull Request

Si quieres contribuir al desarrollo de EvalTrack, puedes hacerlo siguiendo estos pasos:

1. Haz un **fork** de este repositorio.
2. Clona tu fork a tu equipo local:
   ```bash
   git clone https://github.com/TU_USUARIO/EvalTrack.git
   ```
3. Crea una rama nueva para tus cambios:
   ```bash
   git checkout -b mejora/nombre-de-tu-cambio
   ```
4. Realiza tus modificaciones y guarda los cambios con mensajes de commit claros:
   ```bash
   git add .
   git commit -m "Agrega: descripción corta de la mejora"
   ```
5. Sube tus cambios a tu fork:
   ```bash
   git push origin mejora/nombre-de-tu-cambio
   ```
6. Abre un **Pull Request** desde tu repositorio hacia el `main` de este repositorio original.

No olvides incluir una descripción breve de lo que hiciste, por qué lo hiciste y cómo probarlo.

---

¡Gracias por contribuir! Tu apoyo ayuda a que EvalTrack siga creciendo y mejorando. 🚀
