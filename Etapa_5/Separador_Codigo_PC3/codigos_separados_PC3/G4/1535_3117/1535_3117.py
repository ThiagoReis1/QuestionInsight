x = float(input("x: "))
k = int(input("k: "))

c = 0
soma = 0

while c < k:
	termo = ((-1)**c) * ((x ** (2*c + 1)) / (2 * c + 1))
	soma = soma + termo
	c = c + 1
print(round(soma,6))