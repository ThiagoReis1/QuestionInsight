from numpy import*

nota = array(eval(input()))

mfinal = (nota[0] + nota[1] + nota[2] + nota[3]-min(nota))/3.0



print(round(mfinal,2))

if(mfinal>=5.0):
	print("APROVOU")
	
else:
	print("REPROVOU") 


	