x = float(input())
k = int(input())

cont = 0
acum = 0

while(cont < k):
acum = acum + ((-1)**cont)*(x**cont)
	cont = cont + 1
print(round(acum, 7))