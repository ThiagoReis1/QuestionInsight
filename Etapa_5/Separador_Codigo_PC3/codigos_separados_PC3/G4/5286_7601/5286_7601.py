n = int(input("Digite um numero: "))

m = 0
p = 0

while n != 0:
	p = p + 1
	if n % 2 == 0:
		m = m + 1
	n = int(input("Digite um numero: "))

print(p)
x = (m * 100)/(p)
print(round(x,2))
