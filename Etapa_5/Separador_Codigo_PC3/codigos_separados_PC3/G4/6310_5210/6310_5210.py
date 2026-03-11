from numpy import*

x = input().upper()

i = 0
m = 0
p = 0
r = 0
soma = 0

while (i < len(x)):
	if x[i]=='M':
		soma = soma + 7.25
		m +=1
	if x[i]=='P':
		soma = soma + 4.75
		p +=1
	if x[i]=='R':
		soma = soma + 3.5
		r +=1
	i +=1
s = (round(soma, 2))
print(s,m,p,r)