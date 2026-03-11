s = input(": ").upper()
i = 0
cont = 0
while i < len(s):
	if s[i] == 'M':
		print(i)
		cont = cont + 1
	i = i + 1

if cont == 0:
	print("nao achei")

	
