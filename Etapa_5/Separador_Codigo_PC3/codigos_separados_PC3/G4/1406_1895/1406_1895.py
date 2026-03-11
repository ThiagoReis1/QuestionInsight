atk = str(input("Digite o atk: "))
n = int(input("digite o valor de N: "))
t = int(input("Digite o numero de turnos: "))

if( atk == 'cauda'):
	vida = n*t
	print("", vida)
if( atk == 'cuspe'):
	vida = 2*n*t
	print("", vida)