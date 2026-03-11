from numpy import*

v1 = array(eval(input("Informe os valores: ")))
acum = 0
i = 0

while(i<size(v1)):
	if(v1[i] > 80):
		acum += v1[i] * 0.85
	else:
		acum += v1[i]
	i += 1
	
print(round(acum,2))