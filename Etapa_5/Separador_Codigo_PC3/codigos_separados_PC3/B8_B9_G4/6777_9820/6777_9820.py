ano = int(input(''))
pais = (input('(B) ou (I)')).upper()

f = 2023 - ano

if (pais == 'I'):
	if (f >= 17):
		print ('sim')
		ing = f - 17
		print (ing)
	else:
		print ('nao')
		ing = 17 - f
		print (ing)
if (pais == 'B'):
	if (f >= 18):
		print ('sim')
		br = f - 18
		print (br)
	else:
		print ('nao')
		br = 18 - f
		print (br)
elif (pais != 'I') and (pais != 'B'):
	print ('invalido')



