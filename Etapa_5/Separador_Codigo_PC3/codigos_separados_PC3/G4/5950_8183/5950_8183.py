var1 = input("Informe se deseja torta ou pastel (T / P): ")
var2 = int(input("Informe a quantidade de fatias de torta ou pastel: "))
var3 = int(input("Informe a quantidade de cappuccinos: "))

T = 6
P = 5
C = 4.50

if (var1.upper() == 'T'):
	conta = (var2 * T) + (var3 * C)
	
else:
	conta = (var2 * P) + (var3 * C)
	
print(conta)