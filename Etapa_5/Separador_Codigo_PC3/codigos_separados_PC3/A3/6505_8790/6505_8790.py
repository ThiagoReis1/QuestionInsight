# faça seu código aqui!
combos = input("qual dos o tipo de combo 'A', 'B' , 'C': " ).upper()
quantidade = int(input("quantidade de combos: " ))

c = 30 * quantidade
total = c - (15/100*c)

if combos == 'C':
	total = c - (c*15/100)
	print(round(total,2))
else:
	print(c)
	