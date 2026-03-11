sati = input("s ou i ou n ou x: ").upper()
cont = 0
while sati != 'X':
	if sati == 'S':
		cont = cont + 1
	sati = input("s ou i ou n ou x: ").upper()
print(cont)
