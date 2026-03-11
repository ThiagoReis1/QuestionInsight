#Entradas
ta = input("constricao ou polen ?")
nr = int(input("numero de rodadas: "))
d1 = int(input("d1: "))
d2 = int(input("d2: "))

#Condição
if(ta == "constricao"):	
	N = d1+d2
	dano = N + 1
else:
	dano = d1*d2

print(dano)