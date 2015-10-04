import calcplus
import sys
import csv
def main():
    pass


if __name__ == '__main__':
	Calculadora = calcplus.CalculadoraPlus();
	NombreFichero = sys.argv[1];
	with open(NombreFichero) as HojadeCalculo:
		Operaciones = csv.reader(HojadeCalculo)
		for line in Operaciones:
			print(line)
			Operacion = line[0] 
			if Operacion == "sumar" or Operacion == "suma":
				OperacionTotal = 0;
				for next in line:
					if next != "sumar" and next != "suma":
						Calculadora.introAgmt(OperacionTotal,next,Operacion)
						OperacionTotal = Calculadora.sumar()			
	
			if Operacion == "restar" or Operacion == "resta":
				Entrar = True
				OperacionTotal = 0;
				for next in line:
					if next != "restar" and next != "resta":
						Siguiente = next
						Primero = line[1];
						if next == Primero and Entrar:
							Siguiente = -int(next)
							Entrar = False;
						try:
							Siguiente = int(Siguiente);
						except ValueError:
							sys.exit("Non numerical parameters");
						Calculadora.introAgmt(OperacionTotal,Siguiente,Operacion)
						OperacionTotal = Calculadora.restar()

			if Operacion == "multiplicar" or Operacion == "multiplica":
				OperacionTotal = 1;
				for next in line :
					if next != "multiplicar" and next != "multiplica":
						Calculadora.introAgmt(OperacionTotal,next,Operacion)
						OperacionTotal = Calculadora.multiplicar()
			if Operacion == "dividir" or Operacion == "divide":
				OperacionTotal = 1;
				for next in line:
					if next != "dividir" and next != "divide":
						Siguiente = next
						Primero = line[1];
						if next == Primero:
							OperacionTotal = Siguiente
							Siguiente = 1 
						try:
							Siguiente = int(Siguiente);
						except ValueError:
							sys.exit("Non numerical parameters");
						Calculadora.introAgmt(OperacionTotal,Siguiente,Operacion)
						OperacionTotal = Calculadora.dividir()
			
			print(OperacionTotal)

		
		
		

