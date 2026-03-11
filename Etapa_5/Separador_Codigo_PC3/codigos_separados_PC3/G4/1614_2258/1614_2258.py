from numpy import *
vetn = array(eval(input("nomes de alimentos:")))
vetq = array(eval(input("vetor de quantidades gramas:")))

i = 0
tot = 0
while(i<size(vetn)):
	if(vetn[i].upper()=="BANANA"):
		tot = tot + (vetq[i]*0.97) 
	elif(vetn[i].upper()=="BIFE"):
		tot = tot + (vetq[i]*2.95) 
	elif(vetn[i].upper()=="FEIJOADA"):
		tot = tot + (vetq[i]*1.27) 	
	elif(vetn[i].upper()=="OMELETE"):
		tot = tot + (vetq[i]*1.04) 	 
	else:
		tot = tot + (vetq[i]*0.2) 	
	i = i + 1

print(round(tot,2))
		
	