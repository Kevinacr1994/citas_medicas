import csv
import datetime

# Diccionarios para almacenar la información
medicos = {
    "Dr. Pérez": {
        "especialidad": "Cardiología",
        "horario_inicio": "09:00",
        "horario_fin": "15:00",
        "agenda": []
    },
    "Dra. López": {
        "especialidad": "Dermatología",
        "horario_inicio": "10:00",
        "horario_fin": "16:00",
        "agenda": []
    }
}

pacientes = {
    "Juan García": {
        "telefono": "555-1234",
        "citas": []
    },
    "María Martínez": {
        "telefono": "555-5678",
        "citas": []
    }
}

citas = [
    {
        "paciente": "Juan García",
        "medico": "Dr. Pérez",
        "fecha": "2024-09-10",
        "hora": "09:30",
        "confirmada": True,
        "cancelada": False
    },
    {
        "paciente": "María Martínez",
        "medico": "Dra. López",
        "fecha": "2024-09-12",
        "hora": "10:30",
        "confirmada": True,
        "cancelada": False
    }
]

# Función para registrar médicos
def registrar_medico():
    nombre = input("Nombre del médico: ")
    especialidad = input("Especialidad: ")
    horario_inicio = input("Hora de inicio de atención (HH:MM): ")
    horario_fin = input("Hora de fin de atención (HH:MM): ")
    
    medicos[nombre] = {
        "especialidad": especialidad,
        "horario_inicio": horario_inicio,
        "horario_fin": horario_fin,
        "agenda": []
    }
    print(f"Médico {nombre} registrado correctamente.\n")

# Función para registrar pacientes
def registrar_paciente():
    nombre = input("Nombre del paciente: ")
    telefono = input("Teléfono del paciente: ")
    
    pacientes[nombre] = {
        "telefono": telefono,
        "citas": []
    }
    print(f"Paciente {nombre} registrado correctamente.\n")

# Función para verificar disponibilidad
def verificar_disponibilidad(medico, fecha, hora):
    for cita in medicos[medico]["agenda"]:
        if cita["fecha"] == fecha and cita["hora"] == hora:
            return False
    return True

# Función para agendar una cita
def agendar_cita():
    paciente = input("Nombre del paciente: ")
    if paciente not in pacientes:
        print("Paciente no registrado.\n")
        return
    
    medico = input("Nombre del médico: ")
    if medico not in medicos:
        print("Médico no registrado.\n")
        return

    fecha = input("Fecha de la cita (YYYY-MM-DD): ")
    hora = input("Hora de la cita (HH:MM): ")

    if verificar_disponibilidad(medico, fecha, hora):
        cita = {
            "paciente": paciente,
            "medico": medico,
            "fecha": fecha,
            "hora": hora,
            "confirmada": False,
            "cancelada": False
        }
        citas.append(cita)
        medicos[medico]["agenda"].append(cita)
        pacientes[paciente]["citas"].append(cita)
        print(f"Cita agendada para {paciente} con {medico} el {fecha} a las {hora}.\n")
    else:
        print("El médico no está disponible en esa fecha y hora.\n")

# Función para generar un archivo CSV
def generar_csv():
    with open('citas_medicas.csv', mode='w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        
        # Cabeceras
        escritor_csv.writerow(["Paciente", "Médico", "Especialidad", "Fecha", "Hora", "Confirmada", "Cancelada"])
        
        # Agregar datos de citas
        for cita in citas:
            paciente = cita["paciente"]
            medico = cita["medico"]
            especialidad = medicos[medico]["especialidad"]
            fecha = cita["fecha"]
            hora = cita["hora"]
            confirmada = "Sí" if cita["confirmada"] else "No"
            cancelada = "Sí" if cita["cancelada"] else "No"
            
            escritor_csv.writerow([paciente, medico, especialidad, fecha, hora, confirmada, cancelada])
    
    print("Archivo CSV generado: citas_medicas.csv\n")

# Función para cancelar una cita
def cancelar_cita():
    paciente = input("Nombre del paciente: ")
    if paciente not in pacientes:
        print("Paciente no registrado.\n")
        return

    fecha = input("Fecha de la cita a cancelar (YYYY-MM-DD): ")
    hora = input("Hora de la cita a cancelar (HH:MM): ")

    for cita in citas:
        if cita["paciente"] == paciente and cita["fecha"] == fecha and cita["hora"] == hora:
            cita["cancelada"] = True
            print(f"Cita cancelada para {paciente} el {fecha} a las {hora}.\n")
            return
    
    print("No se encontró la cita.\n")

# Función para ver médicos registrados
def ver_medicos():
    print("\nMédicos registrados:")
    for nombre, info in medicos.items():
        print(f"Nombre: {nombre}, Especialidad: {info['especialidad']}, Horario: {info['horario_inicio']} - {info['horario_fin']}")
    print()

# Función para ver médicos disponibles
def ver_medicos_disponibles():
    print("\nMédicos disponibles:")
    hoy = datetime.date.today().strftime("%Y-%m-%d")
    for nombre, info in medicos.items():
        disponible = any(cita["fecha"] == hoy and not cita["cancelada"] for cita in info["agenda"])
        if disponible:
            print(f"Nombre: {nombre}, Especialidad: {info['especialidad']}, Horario: {info['horario_inicio']} - {info['horario_fin']}")
    print()

# Función para ver citas agendadas
def ver_citas_agendadas():
    print("\nCitas agendadas:")
    for cita in citas:
        if not cita["cancelada"]:
            print(f"Paciente: {cita['paciente']}, Médico: {cita['medico']}, Fecha: {cita['fecha']}, Hora: {cita['hora']}")
    print()

# Función para ver citas canceladas
def ver_citas_canceladas():
    print("\nCitas canceladas:")
    for cita in citas:
        if cita["cancelada"]:
            print(f"Paciente: {cita['paciente']}, Médico: {cita['medico']}, Fecha: {cita['fecha']}, Hora: {cita['hora']}")
    print()

# Menú principal
def menu_principal():
    while True:
        print("Sistema de Gestión de Citas Médicas")
        print("1. Registrar médico")
        print("2. Registrar paciente")
        print("3. Agendar cita")
        print("4. Cancelar cita")
        print("5. Generar archivo CSV")
        print("6. Ver médicos registrados")
        print("7. Ver médicos disponibles")
        print("8. Ver citas agendadas")
        print("9. Ver citas canceladas")
        print("10. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_medico()
        elif opcion == "2":
            registrar_paciente()
        elif opcion == "3":
            agendar_cita()
        elif opcion == "4":
            cancelar_cita()
        elif opcion == "5":
            generar_csv()
        elif opcion == "6":
            ver_medicos()
        elif opcion == "7":
            ver_medicos_disponibles()
        elif opcion == "8":
            ver_citas_agendadas()
        elif opcion == "9":
            ver_citas_canceladas()
        elif opcion == "10":
            break
        else:
            print("Opción inválida, intente de nuevo.\n")

# Iniciar el programa
menu_principal()
