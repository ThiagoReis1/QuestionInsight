capacidade = int(input("Insira o numero de containers:"))
estoque =  int(input("Insira o estoque inicial de containers: "))
quantidade = int(input("Insira a quantidade de contaneirs que chegam: "))

semana = 0

while(estoque > 0 ):
	estoque = estoque -capacidade +quantidade
	semana = semana +1
	
print(semana)