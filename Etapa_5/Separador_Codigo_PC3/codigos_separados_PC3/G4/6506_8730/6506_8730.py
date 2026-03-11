# faça seu código aqui!
a = float(input("quantidade de pratos:"))
b = input("sobremesa:")
c = a* 40
if b.lower()== "s":
	d = c - (c *5/100)
	print(round(d,2))
else:
	print(round(c,2))