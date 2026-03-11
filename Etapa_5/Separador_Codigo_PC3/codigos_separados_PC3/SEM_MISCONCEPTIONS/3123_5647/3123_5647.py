from numpy import *

v = array(eval(input('Insira os numeros: ')))

media = 0
i = 0
while (i < size(v)):
	media = media + (v[i]**-1/size(v))
	i = i + 1
print(round(media**-1,2))