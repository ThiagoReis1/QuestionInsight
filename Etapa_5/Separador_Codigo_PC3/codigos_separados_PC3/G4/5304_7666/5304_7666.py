a = float(input())
b = int(input())

aux = 0
while(aux < b):
	a = a + int(a*0.15)
	aux = aux + 1
	print(int(a))