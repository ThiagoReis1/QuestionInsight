from numpy import*
notas = array(eval(input()))
pesos = array([4,3])
num = 0
i = 0
den = sum(pesos)

while i < size (notas):
	num += notas [i] * pesos [i]
	i += 1 

mp = num / den
print(round(mp, 2))