from numpy import*

nome = input ().upper()
v = array(eval(input()))

ar = 1.25*[v]
fe = 2.60*[v]
bi = 1.80*[v]
mi = 0.85*[v]
fa = 3.20*[v]
cf = 0

if (nome==ar):
	cf = cf + 1
elif (nome == fe):
		cf = cf + 1
elif (nome == bi):
		cf = cf + 1
elif (nome == mi):
		cf = cf + 1
else:
	(nome==fa)
	cf = cf + 1

print (cf)
	