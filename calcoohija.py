import sys
import calcoo

class CalculadoraHija(calcoo.Calculadora):
    def multiplicar(self, op1, op2):
	    return op1 * op2

    def dividir(self, op1, op2):
        if op2 == 0:
            sys.exit("Division by zero is not allowed")
        else:  
            return op1 / op2

if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    calculadora = CalculadoraHija()
    if sys.argv[2] == "multiplica":
        result = calculadora.multiplicar(operando1, operando2)
    elif sys.argv[2] == "divide":
        result = calculadora.dividir(operando1, operando2)
    elif sys.argv[2] == "suma":
        result = calculadora.suma(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = calculadora.resta(operando1, operando2)
    else:
        sys.exit('Operación sólo puede ser suma, resta, multiplica o divide.')

    print(result)