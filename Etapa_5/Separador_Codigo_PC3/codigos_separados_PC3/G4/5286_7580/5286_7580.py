x = int(input(': '))
m = cont = 0
while x > 0 :
	if x % 2 == 0:
		m += 1
	cont += 1
	x = int(input(':'))
total = m/cont
print(cont)
print(round(total*100,2))