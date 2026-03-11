s= input("Digite a sequencia: ")

cont= 0

while(s.upper() != "S"):
	if(s.upper() == "A"):
		cont= cont + 1
	s= input("Digite a sequencia: ")
print(cont)
