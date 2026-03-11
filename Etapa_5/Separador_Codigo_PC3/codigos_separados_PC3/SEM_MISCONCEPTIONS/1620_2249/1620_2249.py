from numpy import*
tempo= array(eval(input("")))
percentual= array(eval(input("")))
i=0
var=0
while(i<len(tempo)):
	total= tempo[i]*(percentual[i]/100*5)
	var=var+total
	i = i + 1
print(var)