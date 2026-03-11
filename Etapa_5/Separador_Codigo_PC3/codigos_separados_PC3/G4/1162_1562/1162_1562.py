n = float(input("Digite Premio :"))
c = float(input("taxa rendimento: "))
v = float(input("valor reais: "))
soma = n
t = 1
fim = 0

while (soma > fim):
	rend = (soma * c)
	saldo = (soma+ rend) 
	soma = saldo - v
	t = t + 1
print(t)
	