resultado=input(" qual o resultado ").upper()

conta=0


while(resultado != "X"):
	if(resultado == "A"):
		conta=conta+1
	resultado=input("qual o resultado ").upper()
	
print(conta)