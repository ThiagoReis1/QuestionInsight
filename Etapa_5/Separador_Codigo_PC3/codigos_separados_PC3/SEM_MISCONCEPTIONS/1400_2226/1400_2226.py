ataque = input("contricao ou polen: ")
rod=int(input("num rodadas: "))
D1=int(input("D1: "))
D2=int(input("D2: "))

if(ataque.lower()=="constricao"):
	danos= rod*(D1+D2+1)
else:
	danos= D1*D2

print(danos)
