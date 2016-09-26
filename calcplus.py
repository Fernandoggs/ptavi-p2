import sys
import calcoohija

import csv

with open('fichero.csv')as mifichero:
    datos = csv.reader (mifichero)


if __name__ == "__main__":

    for linea in datos:
        print(linea)

    for linea in mifichero
        operador = linea.split(',')[0]
        print(operador)
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    calculadora = calcoohija.CalculadoraHija()
    if operador == "multiplica":
        result = calculadora.multiplicar(operando1, operando2)
    elif operador == "divide":
        result = calculadora.dividir(operando1, operando2)
    elif soperador == "suma":
        result = calculadora.suma(operando1, operando2)
    elif operador == "resta":
        result = calculadora.resta(operando1, operando2)
    else:
        sys.exit('Operación sólo puede ser suma, resta, multiplica o divide.')

    print(result)