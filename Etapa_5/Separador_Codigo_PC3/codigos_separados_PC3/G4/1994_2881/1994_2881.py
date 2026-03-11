nome = input(" ")
O = 15.9994
C = 12.011
N = 14.00674
H = 1.0079

nome1 = nome.lower()

if nome1== "histidina":
	s = C*6+H*10+N*3+O*2
	print (round(s,2))
elif nome1== "leucina":
	s = C*6+H*13+N+O*2
	print (round(s,2))
elif nome1== "lisina":
	s = C*6+H*15+N*2+O*2
	print (round(s,2))
else:
	print ("Entrada: ",nome)
	print ("Dado Invalido")

