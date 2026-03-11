mi = int(input("A quantidade inicial de moedas:"))
dm = int(input("despesa mensal:"))
m = int(input("impostos:"))
r = int(input("moedas roubadas:"))
soma = mi
t = 0
while(soma > 0):
	soma = soma + m - dm - r
	t = t + 1
print(t)