# faça seu código aqui!
letra = input("digite:").upper()
p = 0
m = 0

while m < len(letra):
	if letra[m] == 'P':
		p+=1
		print(m)
	m+= 1

if p == 0:
	print("nao achei")
		