from numpy import *

A = input("Características Físicas: ").upper().split(",")
preto = 0
castanho = 0
ruivo = 0
loiro = 0
branco = 0
for x in A:
	if x == "P":
		preto = preto + 1
	if x == "C":
		castanho = castanho + 1
	if x == "R":
		ruivo = ruivo + 1
	if x == "L":
		loiro = loiro + 1
	if x == "B":
		branco = branco + 1
		
B = zeros(5, dtype = int)
B[0] = preto
B[1] = castanho
B[2] = ruivo
B[3] = loiro
B[4] = branco
print(max(B))
print(B)
