# Sistema de Gestión de Citas Médicas

Este programa permite gestionar citas médicas, incluyendo la capacidad de registrar médicos y pacientes, agendar y cancelar citas, y generar un archivo CSV con la información de las citas.

## Funcionalidades

1. **Registrar Médico**: Añade un nuevo médico con su especialidad y horario de atención.
2. **Registrar Paciente**: Añade un nuevo paciente con su información de contacto.
3. **Agendar Cita**: Agenda una cita para un paciente con un médico si el médico está disponible.
4. **Cancelar Cita**: Cancela una cita específica.
5. **Generar Archivo CSV**: Crea un archivo CSV con la información de todas las citas.
6. **Ver Médicos Registrados**: Muestra una lista de todos los médicos registrados.
7. **Ver Médicos Disponibles**: Muestra los médicos disponibles para el día actual.
8. **Ver Citas Agendadas**: Muestra todas las citas que no están canceladas.
9. **Ver Citas Canceladas**: Muestra todas las citas que han sido canceladas.

## Uso

1. Ejecuta el programa.
2. Selecciona una opción del menú principal para realizar la acción deseada.
3. Sigue las instrucciones proporcionadas en pantalla.

## Requisitos

- Python 3.x

## Cómo Ejecutar

1. Guarda el código en un archivo, por ejemplo, `sistema_citas.py`.
2. Ejecuta el archivo con el comando:
   ```bash
   python sistema_citas.py

Para registrar un nuevo médico:

Selecciona la opción 1.
Ingresa el nombre del médico, especialidad y horario de atención.
Para agendar una cita:

Selecciona la opción 3.
Proporciona el nombre del paciente, médico, fecha y hora.
Para ver citas agendadas:

Selecciona la opción 8.
Notas
Los datos se almacenan en memoria y se pierden al cerrar el programa.
El archivo CSV se genera en el mismo directorio donde se ejecuta el programa.