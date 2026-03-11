x = float(input("numero real: "))
k = int(input("termos: "))

i = 1
soma = 0

while((i > k)):
	soma = soma + (((-1)**(3 * i)) * (x**i)) / i
	
	i = i + 1
print(round((soma), 10))	
