from numpy import*
var1 = array(eval(input('insira:')))
cod= zeros(size(var1),dtype=int)

for i in range(size(var1)):
	if  var1[i]== 9:
		cod[i] = 0
	else:
		cod[i] = (var1[i] + 1) ** 2
		
print(cod)
