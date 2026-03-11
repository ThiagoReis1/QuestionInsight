x = float(input("Insira um numero real:\n"))
k = int(input("Insira a quantidade de termos:\n"))

i = 0
valor = 0

while(i<k):
	valor = valor + (-1)**i * (x**i)
	i = i + 1
print(round(valor,7))