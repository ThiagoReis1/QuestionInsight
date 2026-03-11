from numpy import *

satisfacao = input("informe se esta satisfeito ou nao: ").upper()
positivo = 0

while(satisfacao != "S"):
	if(satisfacao == "SIM"):
		positivo = positivo + 1

print(positivo)