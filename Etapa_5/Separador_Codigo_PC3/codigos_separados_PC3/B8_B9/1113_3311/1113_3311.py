idade=int(input("Digite:"))
peso=float(input("Digite:"))
print("Entradas:",idade,"anos e",round(peso,1),"kg")
if(idade<0 or idade>130 or peso<0 or peso>550):
	print("Dados invalidos")
else:
	if(idade<=20):
		if(peso<60):
			grupo=9
		elif(peso>=60 and peso<=90):
			grupo=8
		elif(peso>90):
			grupo=7
	elif(idade>20 and idade<=50):
		if(peso<60):
			grupo=6
		elif(peso>=60 and peso<=90):
			grupo=5
		elif(peso>90):
			grupo=4
	elif(idade>50):
		if(peso<60):
			grupo=3
		elif(peso>=60 and peso<=90):
			grupo=2
		elif(peso>90):
			grupo=1
	print("Grupo de risco:",grupo)