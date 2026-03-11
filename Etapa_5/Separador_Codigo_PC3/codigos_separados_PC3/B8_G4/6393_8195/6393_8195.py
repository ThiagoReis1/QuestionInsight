from numpy import * 
var = array(eval(input('')))
for i in range(size(var)):
	if(var[i]== 9):
		var[i] = 0		
	elif(var[i]!= 9):
		var[i] = (var[i] + 1)**3
	
print(var)
	