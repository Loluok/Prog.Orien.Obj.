def calc_segundos():
    horas = int(input('Ingrese las horas: '))
    minutos = int(input('Ingrese los minutos: '))
    segundos = int(input('Ingrese los segundos: '))

    duracion_total = horas * 3600 + minutos * 60 + segundos
    return duracion_total

def convertir_hms(segundos_totales):
    horas = segundos_totales // 3600
    segundos_restantes = segundos_totales % 3600
    minutos = segundos_restantes // 60
    segundos = segundos_restantes % 60
    
    return horas, minutos, segundos

print("1° intervalo de tiempo:")
segundos_1 = calc_segundos()

print("2° intervalo de tiempo:")
segundos_2 = calc_segundos()

total_segundos = segundos_1 + segundos_2

horas_total, minutos_total, segundos_total = convertir_hms(total_segundos)

print(f"La duración total es {horas_total} horas, {minutos_total} minutos y {segundos_total} segundos.")