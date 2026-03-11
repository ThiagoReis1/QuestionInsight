ls = input("L ou S: ").upper()
qtd = int(input("Qtd"))
r = int(input("refri"))

l = qtd*5+r*4
s = qtd*3.5+r*4

if ls=="L":
	print(round(l,2))
else:
	print(round(s,2))