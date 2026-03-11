x = input("insira: ").upper()
m = 0
p = 0
r = 0
t = len(x)-1
i = 0
while i<=t:
	if x[i]== 'M':
		m = m +1
	elif x[i] == 'P':
		p = p +1
	elif x[i] == 'R':
		r = r +1 

	i = i + 1
t= m*7.25 + p*4.75 + r*3.50
print(round(t,2))
		