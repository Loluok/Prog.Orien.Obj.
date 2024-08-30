def calcular_media(numeros):
    if len(numeros) == 0:
        return 0  
    suma = sum(numeros)
    media = suma / len(numeros)
    return media

entrada = input("Ingresa los números separados por espacios: ")

numeros = [float(num) for num in entrada.split()]

media_muestra = calcular_media(numeros)

print("La media de la muestra es:", media_muestra)