x = float(input("digite x"))
k = int(input("digite o termo"))

cont = 1
ap = 1

while(cont < k):
	cont = cont + 1
	ap = ap - ((-1)**(cont))*(x**(cont-1))

print(round(ap,7))
	