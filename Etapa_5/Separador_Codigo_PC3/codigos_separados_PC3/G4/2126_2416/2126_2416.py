from numpy import*
x = array(eval(input('')))
m=(x[0]*5+x[1]*2.5+x[2]*2.5)/10

if m>=5:
	print (round (m,2))
	print("APROVADO")
else:
	 print (round (m,2))
	 print ("REPROVADO")