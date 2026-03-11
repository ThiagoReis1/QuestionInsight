produtos= input("Entre com os produtos: ").upper()
acum= 0
i= 0

while(i < len(produtos):
	if(produtos[i]== "C"):
		acum += 10.50
	elif(produtos[i]== "E"):
		acum += 8.75
	elif(produtos[i]=="P"):
		acum+=17.90
	
	i= i + 1

print(round(acum,2))