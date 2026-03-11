from numpy import *

custo = array(eval(input()))

i = 0
total = 0

while i < len(custo):
	if float(custo[i]) > 80:
		total = total  + (float(custo[i]) - float(custo[i]*0.15))
	elif custo[i] <= 80:
		total = total + float(custo[i])
	i = i + 1	

print(round(total,2))		
	
	