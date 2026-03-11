
consumo = float(input("DIgite o consumo de minutos: "))

if( consumo <= 100):
	valor = 1.2* consumo
else:
	valor = 25 + 1.4 * consumo
print(round(valor,2))