resultado = input("Digite o resultado: ") 
W = 0
D = 0
S = 0

while(resultado.upper() !=  "X"):
	if(resultado.upper() == "V"):
		W  = W + 3
	elif(resultado.upper() == "E"):
		S = S + 2
	elif(resultado.upper() == "D"):
		D = D + 1 
	else:
		x=2
	resultado = input("Digite o resultado: ")
		
print(W)
print(S)
print(D)
	