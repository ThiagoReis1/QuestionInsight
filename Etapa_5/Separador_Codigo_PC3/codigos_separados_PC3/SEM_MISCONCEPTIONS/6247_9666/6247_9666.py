cont = 0

entrada = input().upper()

while entrada != 'X':
	if entrada == 'FT': cont += 1
	
	entrada = input().upper()
	
print(cont)