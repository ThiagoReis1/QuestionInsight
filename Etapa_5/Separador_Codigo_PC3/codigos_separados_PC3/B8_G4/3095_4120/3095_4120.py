r = input("Digite o resultado da partida: ").upper()

w = 0
l = 0
e = 0

while( r != "X"):
	if(r == "V"):
		w = w + 3
		
	elif(r == "E" ):
		e = e + 2
		
	elif(r == "D"):
		l = l + 1
		
	r = input("Digite o resultado da partida: ").upper()
		
print(w)
print(e)
print(l)
