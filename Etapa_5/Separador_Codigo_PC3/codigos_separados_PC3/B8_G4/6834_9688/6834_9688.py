from numpy import*
li = input("Insira a string:").upper()
i = 0
c = 0
p = 0
e = 0
t = len(li)-1

while i <= t:
	if li[i] == 'C':
		c = c+1
	elif li[i] == 'E':
		e = e+1
	elif li[i] == 'P':
		p = p+1
	

	i += 1

t = c*10.50 + e*8.75 + p*17.90

print(round(t,2))