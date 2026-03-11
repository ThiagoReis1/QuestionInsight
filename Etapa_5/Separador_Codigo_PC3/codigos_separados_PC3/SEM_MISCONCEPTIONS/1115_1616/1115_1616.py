from math import *
salario = float(input())
codigo = int(input())

print ("Entradas: R$ ",salario,"e codigo",codigo)

if (salario >= 0):
	if(codigo == 101):
		novo = (salario + (salario * 0.80)/100.00)
		print ("Novo salario: R$ " , round(novo, 2))
	elif (codigo == 102):
		novo = (salario + (salario * 0.65)/100.00)
		print ("Novo salario: R$ " , round(novo, 2))
	elif (codigo == 103):
		novo = (salario + (salario * 0.60)/100.00)
		print ("Novo salario: R$ " ,  round(novo, 2))
	elif (codigo == 104):
		novo = (salario + (salario * 0.55)/100.00)
		print ("Novo salario: R$ " ,  round(novo, 2))
	else : 
			print("Dados invalidos")
else :
	print("Dados invalidos")
	