lanca = int(input("Face do dado: "))

cont = 0
F5 = 0

while(lanca != -1):
	cont = cont + 1
	if(lanca == 5):
		F5 = F5 + 1
	lanca = int(input("Outra face: "))
	
porcentagem = F5/cont*100 

print(cont)
print(round(porcentagem, 2))