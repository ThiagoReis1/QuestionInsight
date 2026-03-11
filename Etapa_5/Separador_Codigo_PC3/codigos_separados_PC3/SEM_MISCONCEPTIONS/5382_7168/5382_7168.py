from numpy import *

plv = input('qual a palavra: ').upper()
vogais = array(['A','E','I','O','U'])
cv = 0
cc = 0
i=0
while i<size(plv):
	if plv[i] == vogais[i]:
		cv = cv * 0.25
		i+=1
	if plv[i] != vogais[i]:
		cc = cc * 0.27
		i+=1
		
	total = cc + cv
	print(round(total,2))

