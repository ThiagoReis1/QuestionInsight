result = input("")
a = result.upper()
soma = 0
jogos = 0
while(a != "X"):      
	if(a == "V"):
		soma = soma + 3
		jogos = jogos + 1
	elif(a == "E"):
		soma = soma + 2
		jogos = jogos + 1
	elif(a == "D"):
		soma = soma + 1
		jogos = jogos + 1
	
	a = input("").upper()
soma = (soma)/(jogos*3) * 100
print(round(soma, 2))
