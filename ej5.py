# Desde máquina

def calc_duracion_segundos(horas, minutos, segundos):

    segundos_horas = horas * 3600
    segundos_minutos = minutos * 60
    duracion_total = segundos_horas + segundos_minutos + segundos

    return duracion_total

horas = 10
minutos = 3
segundos = 45

duracion_segundos = calc_duracion_segundos(horas, minutos, segundos)
print('La duración total en segundos es:', duracion_segundos)

# Pidiendole al usuario

def calc_duracion_segundos():
    horas = int(input('Ingrese las horas: '))
    minutos = int(input('Ingrese los minutos: '))
    segundos = int(input('Ingrese los segundos: '))

    duracion_total = horas * 3600 + minutos * 60 + segundos
    return duracion_total

duracion_segundos = calc_duracion_segundos()

print('La duración total en segundos es:', duracion_segundos)