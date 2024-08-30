# Hola lector! Acá están todos los ejercicios en un mismo archivo ;) Enjoy it


# Ejercicio 1

base = int(input('Ingrese el tamaño de la base del rectángulo: '))
altura = int(input('Ingrese el tamaño de la altura del rectángulo: '))

perimetro = 2 * (base + altura)
area = base * altura

print(f'El perimetro del rectángulo es: {perimetro}')
print(f'El área del rectángulo es: {area}')

# Ejercicio 2

num1 = int(input('Ingrese el primer número: '))
num2= int(input('Ingrese el segundo número: '))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print(f'La suma es: {suma}')
print(f'La resta es: {resta}')
print(f'La multiplicación es: {multiplicacion}')
print(f'La división es: {division}')

# Ejercicio 3

numeros = []

for _ in range(5):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)

numMax = max(numeros)
numMin = min(numeros)

print('Número máximo: ',numMax)
print('Número mínimo: ',numMin)

# Ejercicio 4

numeros = []

for _ in range(5):
    numero = int(input('Ingrese un número: '))
    numeros.append(numero)

hay_duplicados = False

for num in numeros:
    if numeros.count(num) > 1:
        hay_duplicados = True
        break

if hay_duplicados:
    print('Hay números duplicados.')
else:
    print('Hay números distintos.')

# Ejercicio 5

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

# Ejercicio 6