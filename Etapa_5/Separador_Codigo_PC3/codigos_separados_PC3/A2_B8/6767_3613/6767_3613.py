valor = float(input())
codigo = input()

if (codigo.upper()=='D') or (codigo.upper() =='P'):
	valor = valor - valor*0.12
	
elif codigo.upper() == 'C1':
	valor = valor
	
elif codigo.upper() == 'C2':
	valor = valor +valor*0.07

print(round(valor, 2))