h = float(input('valor da heranca:'))
m = float(input('valor fixo sacado:'))
j = float(input('taxa de juros:'))

t = 0

while(h>0)and(m>0)and(j>0):
	v =  m * j
	t = t + 1
print(round(v, 2))
	elif(h<0)or(m<0)or(j<0):
		print('Dados incorretos')