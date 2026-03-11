n = int(input('num: '))

cont = 0
sort = 0

while n != -1:
	cont = cont + 1
	if (n >= 35) and (n <= 95):
		sort = sort + 1
	n = int(input('num: '))

print(sort)