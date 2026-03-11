arma= input("Nome da arma: ")
des= int(input("Destreza do personagem: "))
d1= int(input("Valor sorteado: "))
d2= int(input("Valor sorteado: "))
S= d1+d2


if arma == "sabre" :
	msg = S + (2*des)
else:
	msg = 2*S+des
	
print(msg)