numeros = []

for _ in range(5):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)

numMax = max(numeros)
numMin = min(numeros)

print('Número máximo: ',numMax)
print('Número mínimo: ',numMin)