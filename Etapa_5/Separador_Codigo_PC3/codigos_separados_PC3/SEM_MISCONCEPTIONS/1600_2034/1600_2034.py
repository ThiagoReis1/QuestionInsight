from numpy import*
v= array(eval(input('digite os intens:')))
desconto=15/100
i=0
total=0
while(i<size(v)):
	if(v[i]>80):
		total= total + (v[i]- v[i]*desconto)
		i=i+1
	elif(v[i]<80):
		total= total + (v[i])
		i=i+1
	else:
		print('deu não')
print(round(total,2))	

	
	