from math import*
x = float(input("digite o salario: "))
w = x
w = round(x / 100 * 50,2) + x
if (x == 800.00):
	print (w)
elif ( x >= 800.00) or ( x == 1000.00):
	w = round(x+x*40/100,2)
	print ("Entrada: R$", x)
	print ("Novo salario: R$ ", w)
elif( x > 1000.00 ) or ( x == 1200.00):
	w = round(x+x*30/100,2)
	print ("Entrada: R$", x)
	print ("Novo salario: R$ ", w)
elif ( x >1200.00) or ( x == 1400.00):
	w = round(x+x*20/100,2)
	print ("Entrada: R$", x)
	print ("Novo salario: R$ ", w)
elif ( x >1400.00) or ( x == 1600.00):
	w = round(x+x*10/100,2)
	print ("Entrada: R$", x)
	print ("Novo salario: R$ ", w)
elif ( x > 1600.00):
	w = round(x+x*5/100,2)
	print ("Entrada: R$", x)
	print ("Novo salario: R$ ", w)
elif ( x != 0 /2):
	print("Entrada: R$ ", x)
	print("Dado invalido")