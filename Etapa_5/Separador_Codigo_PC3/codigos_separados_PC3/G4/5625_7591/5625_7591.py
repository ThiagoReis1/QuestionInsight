t = input("tapioca ou salgado")
a = int(input("quantidade de tapiocas ou salgados "))
b = int(input("quantidade de acais "))
if (t == "T"):
	x = a*5.50 + b*10.00
	print(round(x,2))
else:
	y = a*4.00 + b*10.00
	print(round(y,2))
	