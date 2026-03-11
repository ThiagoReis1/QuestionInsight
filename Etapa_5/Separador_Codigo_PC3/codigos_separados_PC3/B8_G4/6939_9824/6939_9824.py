vtc = float(input('digite o valor da compra: '))

cod = input('digite o codigo: ').upper() 

if cod == "D" or cod == "P":
	vf = vtc - (vtc * 0.19)
	print(round(vf,2))
	
elif cod == "C" :
	vezes = int(input('quantidade de vezes: '))
	if vezes == 1:
		vf = vtc 
	else:
		vf = vtc + (vtc * 0.09)

	print(round(vf, 2))