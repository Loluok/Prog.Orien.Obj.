class Persona:

    def __init__(self, nombre, edad, dni):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    def mostrar_edad(self):
        return self.__edad

    def es_mayor_edad(self):
        return self.__edad >= 18

persona = Persona("Lolu", 18, "20323542")

print(f'{persona._Persona__nombre} es mayor de edad' if persona.es_mayor_edad() else f'{persona._Persona__nombre} no es mayor de edad')

