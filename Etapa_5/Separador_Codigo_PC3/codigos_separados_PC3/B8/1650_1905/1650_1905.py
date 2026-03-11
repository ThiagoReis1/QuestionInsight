from numpy import *
v = str(input("Vetor cabelo:")) .upper()
branco = 0
loiro = 0
ruivo = 0
castanho = 0
preto = 0
for x in v:
	if x=="B":
		branco = branco + 1
	elif x=="L":
		loiro = loiro + 1
	elif x=="R":
		ruivo = ruivo + 1
	elif x=="C":
		castanho = castanho + 1
	elif x=="P":
		preto = preto + 1
j = array([preto, castanho, ruivo, loiro, branco])
print(max(j))
print(j)
print(len(v))