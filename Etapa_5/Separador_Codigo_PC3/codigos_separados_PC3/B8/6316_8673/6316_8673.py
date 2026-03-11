produto = input('insira o valor: ')

i = 0

D = 0
S = 0
I = 0
total = 0

while i < len(produto):
	if produto[i] == 'D':
		total += 2.25
		D += 1
	elif produto[i] == 'S':
		total += 4.
		S += 1
	elif produto[i] == 'I':
		total += 6.90
		I += 1
	i += 1
		
print(round(total, 2))
print(D)
print(S)
print(I)
	
	