idade=int(input())
peso=float(input())

i=idade
p=peso

print("Entradas:",i,"anos e",round(p,1),"kg")

if (0<i<=130) and (0.0<p<=550.0):
	if (i<=20 and p<=60):
		print("Grupo de risco: 9")
	if (i<=20 and p>60 and p<=90):
		print("Grupo de risco: 8")
	if (i<=20 and p>90):
		print("Grupo de risco: 7")
	
	if (i>20 and i<=50 and p<=60):
		print("Grupo de risco: 6")
	if (i>20 and i<=50 and p>60 and p<=90):
		print("Grupo de risco: 5")
	if (i>20 and i<=50 and p>90):
		print("Grupo de risco: 4")
	if (i>50 and p<=60):
		print("Grupo de risco: 3")
	if (i>50 and p>60 and p<=90):
		print("Grupo de risco: 2")
	if (i>50 and p>90):
		print("Grupo de risco: 1")
else:
	print("Dados invalidos")
	   