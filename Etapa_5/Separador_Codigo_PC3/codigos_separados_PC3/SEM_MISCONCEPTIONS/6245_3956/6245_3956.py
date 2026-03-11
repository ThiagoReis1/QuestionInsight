entrada = input()
entrada = entrada.upper()
contS = 0
while entrada != 'X':
	if entrada == 'S':
		contS = contS+1
	
	entrada = input()
	entrada = entrada.upper()

print(contS)