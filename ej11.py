import random


class Password:

    __LONGITUD = 8
    __CARACTERES_VALIDOS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"

    def __init__(self, longitud):
        if longitud >= 6 and longitud <= 15:
            self.__longitud = longitud
        else:
            print(f"La contraseña debe de tener entre 6 y 15 caracteres. Se generara una contraseña con la longitud prederterminada ({Password.__LONGITUD})")
            self.__longitud = Password.__LONGITUD
        self.__contrasenia = Password.generarPassword(self)

    @property
    def longitud(self):
        return self.__longitud

    @longitud.setter
    def longitud(self, longitud):
        if longitud >= 6 and longitud <= 15:
            self.__longitud = longitud
            print(f"Longitud cambiada con exito, se generara una nueva contraseña con la longitud ingresada ({self.__longitud})")
            self.__contrasenia = Password.generarPassword(self)
        else:
            print("La contraseña debe de tener entre 6 y 15 caracteres.")

    @property
    def contrasenia(self):
        return self.__contrasenia

    @contrasenia.setter
    def contrasenia(self, contrasenia):
        if len(contrasenia) >= 6 and len(contrasenia) <= 15:
            print("Contraseña cambiada con exito.")
            self.__contrasenia = contrasenia
            self.__longitud = len(contrasenia)
        else:
            print("La contraseña debe de tener entre 6 y 15 caracteres.")

    def generarPassword(self):
        return "".join(random.choice(Password.__CARACTERES_VALIDOS) for i in range(self.__longitud))

    def esFuerte(self):
        tiene_mayuscula = any(c.isupper() for c in self.__contrasenia)
        tiene_minuscula = any(c.islower() for c in self.__contrasenia)
        tiene_numero = any(c.isdigit() for c in self.__contrasenia)
        tiene_especial = any(c in "<=>@#%&+" for c in self.__contrasenia)
        return tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_especial

    def __str__(self):
        return f"Contraseña: {self.__contrasenia} \nEs fuerte?: {"Si" if self.esFuerte() == True else "No"}"


def main():
    passwords = []

    while True:
        longitud = int(
            input("Ingrese la longitud de la contraseña a generar (0 para salir): \n"))
        if longitud == 0:
            break
        password = Password(longitud)
        passwords.append(password)

    for password in passwords:
        print(password)
        print("-----")
    print("Ejercicio Terminado.")


# ------------ Primeras pruebas -------------
""" c1 = Password(10)
print(c1)

print("-----")

c1.longitud = 7
print(c1)
print(c1.longitud)

print("-----")

c1.contrasenia = "Holaaass"
print(c1)
print(c1.contrasenia) """

# --------- main() ---------------
main()