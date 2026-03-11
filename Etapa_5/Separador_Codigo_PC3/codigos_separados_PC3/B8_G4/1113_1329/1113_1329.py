i=int(input("Digite a sua idade:"))
p=float(input("Digite o seu peso:"))
if((i<0)or(i>130)or(p<0)or(p>550)):
	print("Entradas:",i,"anos e",p,"kg")
	print("Dados invalidos")
elif((i<=20)and(p<=60)):
	print("Entradas:",i,"anos e",p,"kg")
	print("Grupo de risco: 9")
elif((i<=20)and(60<p<=90)):
	print("Entradas:",i,"anos e",p,"kg")
	print("Grupo de risco: 8")
elif((i<=20)and(90<p)):
	print("Entradas:",i,"anos e",p,"kg")
	print("Grupo de risco: 7")
elif((20<i<=50)and(p<=60)):
	print("Entradas:",i,"anos e",p,"kg")
	print("Grupo de risco: 6")
elif((20<i<=50)and(60<p<=90)):
	print("Entradas:",i,"anos e",p,"kg")
	print("Grupo de risco: 5")
elif((20<i<=50)and(90<p)):
	print("Entradas:",i,"anos e",p,"kg")
	print("Grupo de risco: 4")
elif((i>50)and(p<=60)):
	print("Entradas:",i,"anos e",p,"kg")
	print("Grupo de risco: 3")
elif((i>50)and(60<p<=90)):
	print("Entradas:",i,"anos e",p,"kg")
	print("Grupo de risco: 2")
elif((i>50)and(90<p)):
	print("Entradas:",i,"anos e",p,"kg")
	print("Grupo de risco: 1")