from numpy import*
li = input("insira a sua lista: ")
i = 0
m = 0
p = 0
r = 0
t = len(li) - 1

while i <= t:
	if li[i] == 'M':
		m = m + 1
	elif li[i] == 'P':
		p = p + 1
	elif li[i] == 'R':
		r = r + 1
	i += 1
t = m*7.25 + p*4.75 + r*3.50
print(round(t , 2))
	