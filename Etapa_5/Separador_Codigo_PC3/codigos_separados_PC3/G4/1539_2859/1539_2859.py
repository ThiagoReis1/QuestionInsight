x = float(input("Escreva um numero real x: "))
k = int(input("Escreva um numero inteiro k: "))

s = 0
i = 0
while(i < k):
	s = s +((-1)**i)*(x**i)
	i = i + 1
	
print(round(s,7))