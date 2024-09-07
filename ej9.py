class ListaDeTareas:

    def __init__(self):
        self.__lista_tareas = []

    def agregarTarea(self, tarea):
        if tarea not in self.__lista_tareas:
            self.__lista_tareas.append(tarea)
            print('Tarea agregada correctamente a la lista')
        else:
            print('La tarea no fue agregada a la lista')

    def quitarTarea(self, tarea):
        if tarea in self.__lista_tareas:
            self.__lista_tareas.remove(tarea)
            print('Tarea eliminada correctamente de la lista')
        else:
            print('La tarea no fue eliminada de la lista')

    def mostrarTarea(self):
        return self.__lista_tareas
        
lista = ListaDeTareas()

# Agrego tareas
lista.agregarTarea('Hacer la cama')
lista.agregarTarea('Salir a caminar')
lista.agregarTarea('Saludar al vecino')
lista.agregarTarea('Meditar')

# Repito una tarea
lista.agregarTarea('Meditar')

# Quito una tarea
lista.quitarTarea('Hacer la cama')

print(lista.mostrarTarea())