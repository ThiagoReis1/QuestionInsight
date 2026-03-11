programa = input('programa').upper()
python = 0

while (programa != 'X'):
	if (programa == 'A'):
		python = python + 1
	
	programa = input('programa').upper()

print(python)
