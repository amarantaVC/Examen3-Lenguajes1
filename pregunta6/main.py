"""
CI3641 - LENGUAJES DE PROGRAMACION I
EXAMEN3 - PREGUNTA 6
AMARANTA VILLEGAS 16-11247
main.py es el modulo principal del interprete del lenguaje prolog
"""

# Importar los modulos necesarios
import re
import Libreria

# Funcion principal
def main():
    print("BIENVENIDO AL INTERPRETE DEL LENGUAJE PROLOG !!!")
    print("Por favor, ingrese una acción (DEF <expresion> [<expresion>])")

    # Variable para controlar el ciclo
    salir = False

    # Crear la base de conocimientos
    dase_datos = Libreria.Base_Datos()  
    
    # Ciclo principal
    while not salir:
        accion = input(">")
        entrada_usuario = accion.strip()
        partes = entrada_usuario.split(' ', maxsplit=1)
        accion = partes[0].upper()
        
        # Procesar la acción DEF ingresada por el usuario
        if accion == 'DEF':
            if len(partes) > 1:
                expresiones = re.findall(r'(\w+\([^)]+\))', partes[1])
                expresiones_parseadas = list(map(str.strip, expresiones))

                Libreria.procesar_def(expresiones_parseadas, dase_datos)
                print()
            else:
                print("ERROR: La acción 'DEF' necesita al menos una expresión")
        # Procesar la acción ASK ingresada por el usuario
        elif accion == 'ASK':
            if len(partes) > 1:
                Libreria.procesar_consulta(partes[1], dase_datos)
            else:
                print("ERROR: La acción 'ASK' necesita una expresión")
        
        # Procesar la acción SALIR ingresada por el usuario
        elif accion == 'SALIR':
            salir = True

        # indicamos que la acción ingresada no es valida
        else:
            print("ERROR: Accion no valida ")


# Iniciar el programa
if __name__ == "__main__":
    main()
