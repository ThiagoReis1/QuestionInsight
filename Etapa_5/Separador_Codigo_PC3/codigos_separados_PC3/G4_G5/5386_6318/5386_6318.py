from numpy import*
p = input("s: ").upper()
def conta_vogais(string):
	v = 0
	vogais = 'AEIOU'
	for i in vogais:
		v = v + string.count(i)
	return v
def conta_consoante(string):
	c = 0
	con = 'QWRTYPSDFGHJKLZXCVBNM'
	for i in con:
		c = c + string.count(i)
	return c
a = conta_vogais(p)*1.12
b = conta_consoante(p)*1.18
d = a + b
print(round(d,2))
