p = int(input(":"))
v = int(input(":"))
t = int(input(":"))

s = p + v * t

if(s>=(p+1000)):
	print(s)
	print("Sim")
else:
	print(s)
	print("Nao")