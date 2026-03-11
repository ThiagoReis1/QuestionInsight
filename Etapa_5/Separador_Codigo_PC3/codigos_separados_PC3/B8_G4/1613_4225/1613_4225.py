from numpy import*

va = array(eval(input( )))
vm = array(eval(input( )))
kcal = 0
i = 0
while(i<size(va)):
	if(va[i]=="ALONGAMENTO"):
		kcal = kcal+(3.0*vm[i])
	elif(va[i]=="CORRIDA"):
		kcal = kcal+(10.3*vm[i])
	elif(va[i]=="DANCA"):
		kcal = kcal+(6.7*vm[i])
	elif(va[i]=="ESCALADA"):
		kcal = kcal+(9.7*vm[i])
	elif(va[i]=="HIDROGINASTICA"):
		kcal = kcal+(5.0*vm[i])
	i = i+1
print(round(kcal,2))