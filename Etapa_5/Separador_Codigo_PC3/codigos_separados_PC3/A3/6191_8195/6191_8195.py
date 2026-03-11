var1 = input('')
coroa = 0
cara = 0
while(var1.upper() != 'S'):
	if(var1 == 'CARA'):
		cara = cara + 1
	var1 = input('')
print(cara)