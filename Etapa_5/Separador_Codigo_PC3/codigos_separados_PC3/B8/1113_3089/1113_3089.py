from math import*
idade=int(input("qual a idade: "))
peso=float(input("qual o peso: "))
print("Entradas:",idade,"anos e",peso,"kg")
m="Grupo de risco:"
if(((idade>=0)and(idade<=130))and((peso>=0.0)and(peso<=550.0))):
	if((idade<=20)and(peso<=60)):
		print(m,9)
	elif((idade<=20)and(peso>60 and peso<=90)):
		print(m,8)
	elif((idade>=0)and(peso>90)):
		print(m,7)
	elif((idade>20 and idade<=50)and(peso<=60)):
		print(m,6)
	elif((idade>20 and idade<=50)and(peso>60 and peso<=90)):
		print(m,5)
	elif((idade>20 and idade<=50)and (peso>90)):
		print(m,4)
	elif((idade>50)and(peso<=60)):
		print(m,3)
	elif((idade>50)and(peso>60 and peso<=90)):
		print(m,2)
	elif((idade>50)and(peso>90)):
		print(m,1)
else:
	print("Dados invalidos")