n = int(input())

cont = 1
soma = 0

while cont <= n:
	soma += cont**3
	cont += 1
	
print("soma=", soma)