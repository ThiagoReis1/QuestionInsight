from numpy import *

aneis = array(eval(input()))
i = 0
total = 200

while i < len(aneis):
	if float(aneis[i]) == 1 :
		total = total*4
	elif float(aneis[i]) == 2 :
		total = total*2
	elif float(aneis[i]) == 3 :
		total = total	
	elif float(aneis[i]) == 4 :
		total = total/2		
	i = i + 1
	
print(round(total,2))