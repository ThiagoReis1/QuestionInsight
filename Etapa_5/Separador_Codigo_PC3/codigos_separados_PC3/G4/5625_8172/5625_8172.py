item = input().upper()
qtde = int(input())
acai = int(input())

if item == 'T':
	total = (qtde*5.50) + acai*10
	print(round(total,1))
else:
	total = qtde*4 + acai*10
	print(round(total,1))