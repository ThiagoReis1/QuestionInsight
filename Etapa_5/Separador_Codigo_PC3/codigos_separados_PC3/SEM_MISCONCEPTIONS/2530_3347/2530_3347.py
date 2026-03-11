D = float(input("deposito: "))
TF = float(input("tarifa fixa: "))
j = float(input("juros: "))/100

saldo = 0
n = 0

if ( D>0) and (TF > 0) and (j > 0):
	while ( saldo < (0.15*D)+D):
		
	