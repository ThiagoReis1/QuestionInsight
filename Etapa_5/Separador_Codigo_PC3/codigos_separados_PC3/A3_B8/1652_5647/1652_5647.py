from numpy import *

etnia = input('Insira as etnias: ').split(',')

quant = 0
quantB = 0
quantPA = 0
quantPR = 0
quantA = 0
quantI = 0

B = 'B'
PA = 'PA'
PR = 'PR'
A = 'A'
I = 'I'

v = zeros(5, dtype=int)

for i in range(size(etnia)):
	if etnia[i] == B:
		quantB = quantB + 1
		v[0] = quantB
	elif etnia[i] == PA:
		quantPA = quantPA + 1
		v[1] = quantPA
	elif etnia[i] == PR:
		quantPR = quantPR + 1
		v[2] = quantPR
	elif etnia[i] == A:
		quantA = quantA + 1
		v[3] = quantA
	elif etnia[i] == I:
		quantI = quantI + 1
		v[4] = quantI
print(max(v))
print(v)