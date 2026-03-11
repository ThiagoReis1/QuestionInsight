resultado = input().upper()
a = 0

while(resultado != 'X'):
	if(resultado == 'A'):
		a = a + 1
		
	resultado = input().upper()

print(a)