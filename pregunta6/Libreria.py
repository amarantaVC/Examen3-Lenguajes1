"""
CI3641 - LENGUAJES DE PROGRAMACION I
EXAMEN3 - PREGUNTA 6
AMARANTA VILLEGAS 16-11247
Libreria.py es un modulo que contiene las clases y funciones necesarias para el funcionamiento del interprete
"""

import re

# Parte a. Debe saber manejar hechos, reglas y consultas.

#clase para validar la expresion ingresada por el usuario
class Expresion:
    def __init__(self, exp_str):
        self.exp_str = exp_str.strip()
        self.tipo = self.expresion_valida()

    def expresion_valida(self):
        # Cualquier cadena alfanumérica que empiece con un caracter en minúscula la consideramos un ÁTOMO.
        if re.match(r'^[a-z][a-zA-Z0-9_]*$', self.exp_str): 
            return "Átomo"
        elif re.match(r'^[A-Z][a-zA-Z0-9_]*$', self.exp_str): # Cualquier cadena alfanumérica que empiece con un caracter en mayúscula la consideramos una VARIABLE.
            return "Variable"
        elif re.match(r'^[a-z][a-zA-Z0-9_]*\((.*)\)$', self.exp_str): 
            # Un átomo, seguido de una secuencia, parentizada y separada por comas, de otras expresiones la consideramos una ESTRUCTURA.
            return "Estructura"
        else:
            return "ERROR: Expresión no válida"


#definimos la clase hecho
class Hecho:
    def __init__(self, nombre_predicado, args):
        self.nombre_predicado = nombre_predicado
        self.args = args

#definimos la clase regla 
class Regla:
    def __init__(self, nombre_predicado, args, antecedentes):
        self.nombre_predicado = nombre_predicado
        self.args = args
        self.antecedentes = antecedentes

#definimos la clase predicado
class Predicado:
    def __init__(self, nombre, args):
        self.nombre = nombre
        self.args = args
        
#esta clase almacena los hechos y las reglas
class Base_Datos:
    def __init__(self):
        self.hechos = []
        self.reglas = [] 

    #agregamos los hechos y las reglas
    def agregar_hecho(self, hecho):
        self.hechos.append(hecho)

    def agregar_regla(self, regla):
        self.reglas.append(regla)

# Esta función procesa la acción DEF ingresada por el usuario y la almacena en la base de conocimientos
def procesar_def(expresiones, base):
    if len(expresiones) == 1:
        # Verificar si es un hecho
        coincidencia = re.match(r'^\s*(\w+)\s*\(([^)]*)\)\s*$', expresiones[0])
        if coincidencia:
            nombre_predicado, args = coincidencia.groups()

            # Crear un objeto de hecho
            hecho = Hecho(nombre_predicado, args.split(','))

            # Agregar el hecho a la base de conocimientos
            base.agregar_hecho(hecho)

            print(f"Se definió el hecho '{nombre_predicado}({args})'")
        else:
            print("ERROR: expresión mal bien formada")
    else:
        # Verificar si es una regla
        coincidencia = re.match(r'^\s*(\w+)\s*\(([^)]*)\)\s*$', expresiones[0])
        if coincidencia:
            nombre_predicado, args = coincidencia.groups()
            antecedentes = expresiones[1:]
            antecedentes_str = ", ".join(map(str.strip, antecedentes))


            # Crear un objeto de regla
            regla = Regla(nombre_predicado, args.split(','), antecedentes)
            # Agregar la regla a la base de conocimientos
            base.agregar_regla(regla)

            print(f"Se definió la regla '{nombre_predicado}({args}) :- {antecedentes_str}'")
        else:
            print("ERROR: expresion mal bien formada")


# Esta función procesa la acción ASK ingresada por el usuario y la evalúa en la base de conocimientos
def procesar_consulta(expresion, dase_datos):

    coincidencia = re.match(r'^\s*(\w+)\s*\(([^)]*)\)\s*$', expresion)

    if coincidencia:
        nombre_predicado, args = coincidencia.groups()
        predicado = Predicado(nombre_predicado, args.split(','))
        
        # Verificar si la expresión está bien formada para una consulta
        if not args or all(re.match(r'^[a-zA-Z]\w*$', arg.strip()) for arg in args.split(',')):

            print("ERROR: expresión mal formada")
            return

        else:
            print("No es satisfacible.")
    else:
        print("ERROR: La expresión mal formada")

