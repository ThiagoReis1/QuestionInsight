nm = int(input())
l = 0
c = 0
p = 0
n = 0

while n < nm:
	o = input('opcao').upper()
	n = n + 1
	
	if o == 'L':
		l = l + 1
	elif o == "C":
		c = c + 1
	elif 0 == "P":
		p = p + 1
print("L=", l)
print("C=", c)
print('P=', p)