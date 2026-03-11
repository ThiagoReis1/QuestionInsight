tipo = input().upper()

cont= 0

while tipo != "X":
	if tipo == "A":
		cont+=1
	tipo = input().upper()
	
print(cont)