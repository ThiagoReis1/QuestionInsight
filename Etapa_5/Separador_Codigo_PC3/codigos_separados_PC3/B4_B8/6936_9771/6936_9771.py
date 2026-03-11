total = float(input())
codigo = input()

if codigo == 'D':
	final = total - (total * (13/100))
elif codigo == 'P':
	final = total - (total *(13/100))
elif codigo == 'C':
	parcela = int(input())
	if parcela == 1:
		final = total
	elif parcela == 2:
		final = total + (total * (8/100))
	
print(round(final, 2))
