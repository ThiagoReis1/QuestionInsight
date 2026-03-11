from numpy import*

s = input(": ")

v = 'aeiou'

conta = 0
conte = 0
conti = 0
conto = 0
contu = 0

for i in range(len(s)):
	if s[i] == 'a':
		conta = conta + 1
	elif s[i] == 'e':
		conte = conte + 1
	elif s[i] == 'i':
		conti = conti + 1
	elif s[i] == 'o':
		conto = conto + 1
	elif s[i] == 'u':
		contu = contu + 1
		
print('a:', conta)
print('e:', conte)
print('i:', conti)
print('o:', conto)
print('u:', contu)
	