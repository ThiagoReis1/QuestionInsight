vc = float(input("Valor consumido: "))

if vc <= 300:
	x = (vc*.1)+vc
else:
	x = (vc*.06)+vc
print(round(x,2))	