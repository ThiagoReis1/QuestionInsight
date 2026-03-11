atual = float(input("salario :"))
if (atual <= 800):
	novo = atual + (atual/100 *50)
	print("Entrada :R$",atual,)
	print("Novo salario: R$",novo)	
elif (atual >800 ) and (atual <= 1000):
	novo = atual + (atual/100 *40
	print("Entrada :R$",atual,)					 
   print("Novo salario: R$",novo´
elif (atual > 1000) and (atual <=1200):
	novo = atual + (atual/100 *30)
	print("Entrada :R$",atual,)
	print("Novo salario: R$",novo)
elif (atual > 1200) and (atual <=1400):
	novo = atual + (atual/100 *20)
	print("Entrada :R$",atual,)
	print("Novo salario: R$",novo,)
elif (atual > 1400) and (atual <=1600):
	novo = atual + (atual/100 *10)
	print("Entrada :R$",atual,)
	print("Novo salario: R$",novo,)
elif (atual > 1600): 
   novo =  atual + (atual/100 *5)
	print("Entrada :R$",atual,)
	print("Novo salario: R$",novo,
else:
	print("Entrada: R$",atual)
	print("Dado invalido")