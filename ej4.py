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