def agregar_una_vez(lista, elem):

    if elem in lista:
        raise ValueError(f"Error: Imposible añadir elementos duplicados => {elem}")
    else:
        lista.append(elem)

def main():
    elementos = [1, 5, -2]
    try:
        agregar_una_vez(elementos, 10)
        agregar_una_vez(elementos, -2) 
        agregar_una_vez(elementos, "Hola")
    except ValueError as e:
        print(e)
        print(elementos)

if __name__ == "__main__":
    main()