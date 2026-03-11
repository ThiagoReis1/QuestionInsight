num = int(input('digite um numero:'))
x = num//100
y = num%100
if(((x + y)**2) == num):
	msg = 'atende'
	print(num)
	print(msg)
else:
	msg = 'nao atende'
	print(num)
	print(msg)
