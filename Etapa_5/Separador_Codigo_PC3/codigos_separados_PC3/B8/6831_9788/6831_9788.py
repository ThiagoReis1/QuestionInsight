itens = input('produtos: ').upper()

i = 0 
total = 0 
while i <len(itens):
	if itens[i] == 'A':
		total += 16.75
	elif itens [i] == 'L':
		total += 4.6
	elif itens [i] == 'P':
		total += 2.85
	i +=1
print(round(total,2))