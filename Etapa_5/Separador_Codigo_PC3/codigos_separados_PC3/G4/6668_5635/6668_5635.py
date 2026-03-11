from numpy import *
p = (eval(float(input("material: "))))
s = 0
q = 0

for preco in precos: 
	if p > 170:
		s += p
		q += 1
	if q > 0:
		media = round(s/q, 2)
else: 
	media = 0.0
print(media)
		