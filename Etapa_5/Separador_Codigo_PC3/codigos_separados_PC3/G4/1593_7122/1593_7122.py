from numpy import*
v = array(eval(input("")))

i = 0
som = 0
peso = 0

while (i < size(v)):
	som = som + v[i] * (i+1)
	peso = peso + i + 1
	i = i + 1
mp = som/peso

print(round(mp,2))