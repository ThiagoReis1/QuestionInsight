a = input("oq comer:")
b = int(input("quantidade:"))
d = int(input("quant suco:"))
if a.lower()== "c":
	e = b*2 + d*6
	print(round(e,2))
else:
	f = b*4.5 + d*6
	print(round(f,2))