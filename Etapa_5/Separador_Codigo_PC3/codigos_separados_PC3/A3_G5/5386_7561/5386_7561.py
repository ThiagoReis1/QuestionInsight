from numpy import*
se = input ("senha:").upper()
def conta_vogais(string):
	v= 0
	vogais= 'aeiou'
	for i in vogais:
		v += string.count(i)
		return (v)
def cont_consoante(string):
	c =0
	consoante = 'bcdfghjklmnpqrstvwxyz'
	for i in conso:
		c += string.count(i)
		return (c)
print(cont_vogais(se))
print (cont_consoante(se))