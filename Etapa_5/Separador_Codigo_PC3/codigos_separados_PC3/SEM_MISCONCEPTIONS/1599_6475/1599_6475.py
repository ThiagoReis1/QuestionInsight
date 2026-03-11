from numpy import *
ci= array(eval(input('type of values : ')))
i= 0
tamanho= len(ci)

while (i<tamanho):
	if (ci[i]>80):
		ci[i]= ci[i]-(ci[i]*0.15)
		i= i+1
	else:
		i= i+1
		
total= sum(ci)
print(round(total,2))