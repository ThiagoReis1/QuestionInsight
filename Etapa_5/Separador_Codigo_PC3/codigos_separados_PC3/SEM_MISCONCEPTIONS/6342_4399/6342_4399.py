string = str(input())

prim_caract = string[0]

if prim_caract == 'm' or prim_caract == 'M':
	string = string.upper()
	print(string)
else:
	print("nome invalido")