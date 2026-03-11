x = float(input(""))
k = int(input(""))
exp = 0
termo = 0
soma = 0
while(termo < k):
	soma = soma + (-1**exp) * (x * exp)
	termo = termo + 1
	exp = exp + 1
print(round(soma, 7))

	
	