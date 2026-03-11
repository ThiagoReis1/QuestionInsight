from numpy import*
custo = array(eval(input("")))

i=0
total=0
while i <size(custo):
	if custo[i]>80:
		pre=(custo[i]/100)*85
		total=pre+total
		
	else:
		total=total+custo[i]	
	i=i+1

print(round(total,2))	