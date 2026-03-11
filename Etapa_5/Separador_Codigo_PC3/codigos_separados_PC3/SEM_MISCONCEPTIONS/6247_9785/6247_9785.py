
contador_ft = 0
entrada = input("").upper()

while entrada != 'X':
	if entrada == 'FT':
		contador_ft += 1
	entrada = input("").upper()
	
print(contador_ft)
