p = input(" ").upper()

contador = 0

while(p != "X"):
	if(p == "S"):
		contador = contador + 1
	p = input (" ").upper()
	
print(contador)