x = float(input("x: "))
k = int(input("k: "))
cont = 1
s = 0

while(cont <= k):
	s = s + (cont/(2 * cont * x))
	cont = cont + 1
print(round(s,10))