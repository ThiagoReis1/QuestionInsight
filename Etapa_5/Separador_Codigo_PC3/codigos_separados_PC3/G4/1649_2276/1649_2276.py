from numpy import*
o = input("")
x = o.split(',')
#P – Preto
#C – Castanho
#M – Mel
#V – Verde
#A – Azul
p = 0
c = 0
m = 0
v = 0
a = 0
l = zeros(5, dtype = int)
for i in x:
	if i == "P":
		p = p + 1
	if i == "C":
		c = c+ 1
	if i == "M":
		m = m +1
	if i == "V":
		v = v + 1
	if i == "A":
		a = a + 1
l[0] = p
l[1] = c
l[2] = m
l[3] = v
l[4] = a
print(int(max(l)))
print(l)