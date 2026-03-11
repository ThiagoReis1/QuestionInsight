n = int(input("digite um ano: "))
pais = input("b ou P: ").upper()


if n < 2003 and pais == 'b':
	soma = 2023 - n - 21
	print('sim')
	print(soma)
	
elif  n > 20031 and pais == 'b' :
	soma = 2023 - n - 21
	print('nao')

elif pais == 'E' and 'E' >= 18:
	soma = 2005 - n - 18
	print('sim')
	
	

elif pais == 'E' and 'E'< 18:
	print('nao')
	
else: 
	print('invalido')
	
