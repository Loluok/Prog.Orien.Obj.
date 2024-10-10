import random

class Password:
    __LONGITUD = 8
    __CARACTERES_VALIDOS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"   

    def __init__(self, longitud):
        if longitud >= 6 and longitud <= 15:
            self.__longitud = longitud
        else:
            print('La longitud debe ser de 6 a 15 caracteres. Se generará una contraseña de longitud 8.')
            self.__longitud = Password.__LONGITUD

        self.__contrasenia = self.generarPassword()

# GenerarPassword: Retorna un String vacio al cual se le concatena(Join()) un caracter random elegido(random.choice), 
# del atributo CARACTERES_VALIDOS de la clase Password, y esto se repite tanta veces como valor reciba el atributo de instancia privado longitud.

    def generarPassword(self): 
        return "".join(random.choice(Password.__CARACTERES_VALIDOS) for i in range(self.__longitud))

    def esFuerte(self):
        mayuscula = 0
        minuscula = 0
        numero = 0
        caracter_especial = 0
        for c in self.__contrasenia:
            if c.isupper(): 
                mayuscula += 1
            elif c.islower():  # elif: sino
                minuscula += 1
            elif c.isdigit():
                numero += 1
            else:
                caracter_especial += 1

        return mayuscula >= 1 and minuscula >= 1 and numero >= 1 and caracter_especial >= 1 # agiliza el código, en vez de poner otro if que retorne directo un T o F, acá lo hace directamente
    
    def __str__(self):
        return f'{self.__contrasenia} -- {self.esFuerte()}'

    def getPassword(self):
        return self.__contrasenia
    
    def getLongitud(self):
        return self.__longitud
    
    def setLongitud(self, longitud):
        if longitud >= 6 and longitud <= 15:
            print('La longitud se ha cambiado correctamente.')
            self.__longitud = longitud
            self.__contrasenia = self.generarPassword()
        else: 
            print('La contraseña debe ser de 6 a 15 carácteres.')

    def setPassword(self, contrasenia):
        if len(contrasenia) >= 6 and len(contrasenia) <= 15:
            print('La contraseña se cambió exitosamente.')
            self.__longitud = len(contrasenia)
            self.__contrasenia = contrasenia
        else:
            print('La contraseña debe tener entre 6 a 15 carácteres.')

# prueba = Password(9)
#print(prueba)
#print('\n') # Salto de línea. \ ayuda a poner carácteres especiales.
#prueba.setLongitud(8)
#print(prueba) # Siempre imprimir
#print(prueba.getLongitud())
#print('\n')
#prueba.setPassword('32kkKW#')
#print(prueba)
#print(prueba.getPassword()) """

contrasenia = []

while True: 
    longitud = int(input('Ingrese la longitud de la contraseña a generar (0 para salir): \n'))
    if longitud == 0:
        break

    contrasenia.append(Password(longitud))

for i in range(len(contrasenia)):
    print(contrasenia[i])