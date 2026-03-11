respostas = input("qual o total de respostas? ").upper()
	
cont = 0
clientes = 0

while respostas != "X":
	if respostas == "S":
		cont += 1 
	respostas = input("qual o total de respostas? ").upper()
	
print(cont)
	
