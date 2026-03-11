programa = input('').upper()

quantidade = 0

while programa != 'X':
	if programa == 'A':
		quantidade += 1
	programa = input('').upper()
	
print(quantidade)