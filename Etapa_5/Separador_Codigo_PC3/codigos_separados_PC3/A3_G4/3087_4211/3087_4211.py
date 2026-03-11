x = int(input("Digite um numero: "))
n = 0
i = 0
while(x != 0):
	x = int(input())
	n = n + 1
	if(x%2 == 0):
		mx = (n*x)/n
	else:
		m2 = x / n
print(round(mx, 2))
print(round(m2, 2))