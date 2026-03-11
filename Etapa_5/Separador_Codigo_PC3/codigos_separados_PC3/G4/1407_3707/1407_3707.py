vida = int(input())
d1 = int(input())
d2 = int(input())
d3 = int(input())
n = d1 + d2 + d3
vida = vida - 10*n

if vida <= 0:
	print(0)
	print('MOR')
else:
	print('0')
	print('MORTO')

