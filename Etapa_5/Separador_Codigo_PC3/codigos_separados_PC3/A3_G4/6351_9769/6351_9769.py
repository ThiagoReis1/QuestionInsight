from numpy import*

name =input('').upper()

i =0
cont = 0

if name[-1] == "s" or name[-1] == "S":
	name = name.upper()
	print(name)

else:
	print('nome invalido')