x = float(input("digite o valor: "))
k = int(input("digite o valor: "))


while (-1 < x < 1) and (k>0):
	x = 1/1+x
	k = x + 1
print(round(x,7))