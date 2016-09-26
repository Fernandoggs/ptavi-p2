import sys
import calcoohija
import csv




if __name__ == "__main__":

    with open('fichero.csv')as mifichero:
        datos = csv.reader (mifichero)
        calculadora = calcoohija.CalculadoraHija()
        for linea in datos:
            #print(linea)

            for palabra in linea:
                operador = palabra
                #print(operador)
                linea.pop(0)
                if operador == "suma":
                    result = 0
                    print("Result suma:")
                    for numero in linea:
                        result = calculadora.sumar(result,int(numero))

                elif operador == "resta":
                    result = int(linea[0])
                    print("Result resta")
                    linea.pop(0)
                    for numero in linea:
                        result = calculadora.restar(result,int(numero))

                elif operador == "multiplica":
                    result = int(linea[0])
                    print("Result multiplica")
                    linea.pop(0)
                    for numero in linea:
                        result = calculadora.multiplicar(result,int(numero))

                elif operador == "divide":
                    result= int(linea[0])
                    print("Result divide")
                    linea.pop(0)
                    for numero in linea:
                        result = calculadora.dividir(result,int(numero))
                        

            print(result)