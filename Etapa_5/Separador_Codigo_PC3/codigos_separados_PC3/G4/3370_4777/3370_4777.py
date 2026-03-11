uni1 = input("o valor da unidade: ")
vm = float(input(" valor da media:"))

if uni1 == "P":
	c = vm/0.393701
	print(round(c, 2))
	
else:
	p = 0.393701 * vm
	print(round(p, 2))