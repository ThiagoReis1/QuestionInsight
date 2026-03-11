from math import*
vm = float(input("Qual o valor da mensalidade em reais ? : "))
n = int(input("Qual o numero de criancas na familia ? : "))

if	(n == 1):
	vt = (vm * n) - (((vm * n) * 10) / 100)
		
elif	(n == 2):
	vt = (vm * n) - (((vm * n) * 30) / 100)
	
elif	(n >= 3):
	vt = (vm * n) - (((vm * n) * 40) / 100)
	
	
print(round(vt, 2))
