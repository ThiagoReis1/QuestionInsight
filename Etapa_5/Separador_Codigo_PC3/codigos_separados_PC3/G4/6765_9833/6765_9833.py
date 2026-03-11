H = int(input())
pais = input().upper()

if pais == 'B':
	if 2023 - H >= 18:
		print('sim')
		var1 = (2023 - H) - 18
		print(var1)
	else:
		print('nao')
		var1 = 18 - (2023 - H)
		print(var1)
elif pais == 'R':
	if 2023 - H <= 21:
		print('sim')
		var1 = 21 - (2023 - H)
		print(var1)
	else: 
		print('nao')
		var1 = 21 - (2023 - H)
		print(var1)
else: 
	print ('invalido')
