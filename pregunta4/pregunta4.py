"""
CI3641 - LENGUAJES DE PROGRAMACION I
EXAMEN3 - PREGUNTA 4
AMARANTA VILLEGAS 16-11247
Archivo pregunta4.py: Manejador de tablas de métodos virtuales para un sistema orientado a objetos con herencia simple y despacho dinámico de métodos
"""



import sys

# Clase para las clases
class Class:

    def __init__(self, name, methods: list, parent = None):
        self.name,self.parent,self.finalMethods = name, parent, {}

        if type(parent) == Class:
            self.finalMethods = parent.finalMethods.copy()

        for method in methods:
            self.finalMethods[method] = name

# Clase de la tabla de métodos virtuales
class Table:

    def __init__(self):
        self.table = {}

    def declare(self, action: list):
        className = action[0]

        if className not in self.table:

            if action[1] == ":":

                parentName = action[2]

                if parentName in self.table:

                    parent = self.table[parentName]
                    methods = action[3:]

                else:
                    return f"Error: {parentName} no existe"

            else:
                parent = None
                methods = action[1:]

            # Se verifica si se repite algún nombre de metodo:
            #temp = [x for x in methods if methods.count(x) <= 1]
            seen = set()
            temp = [x for x in methods if x not in seen and not seen.add(x)]


            if len(methods) > len(temp):
                return f"Error: los metodos deben tener nombres diferentes"

            # Se crea una nueva clase que hereda del padre:
            classNew = Class(className, methods, parent)

            # Se guarda esta nueva clase en la tabla:
            self.table[className] = classNew

            return f"La clase {className} se definió con los metodos -> {classNew.finalMethods}"

        else:
            return f"Error: {className} ya existe"

    def describe(self, action: str):

        if action[0] in self.table:

            className = self.table[action[0]]
            methods = className.finalMethods.copy()

            sol_lines = []
            for metodo, valor in methods.items():
                sol_lines.append(f'{metodo} -> {valor} :: {metodo}')

            sol = '\n'.join(sol_lines)

            return sol

        else:

            return f"Error: {action[0]} no existe"


# Programa principal
table = Table()

def main(action):

    action = action.strip().split()

    if action[0] == "CLASS":
        out = table.declare(action[1:])

    elif action[0] == "DESCRIBIR":
        out = table.describe(action[1:])

    elif action[0] == "SALIR":
        sys.exit()

    else:
        out = "Error: accion invalida"

    return out


if __name__ == "__main__":

    while True:

        print("\nIngrese una accion: \nDeclarar clase: CLASS <tipo> [<nombre>] \nDescribir clase: DESCRIBIR <nombre> <expr>\nSalir: SALIR\n")

        action = input()

        print(f'{main(action)}')
