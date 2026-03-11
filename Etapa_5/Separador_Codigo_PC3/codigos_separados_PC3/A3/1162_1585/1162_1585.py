n = float(input("Digite o valor do premio:"))
juros = float(input("Digite o valor do juros"))
gasto = float(input("Digite o valor esbanjado mensalmente:"))
q = 0
t = 1
while(n >= 0):
	rend = (n / 100) * juros
	q = rend + q
	t = t + 1
print(t)