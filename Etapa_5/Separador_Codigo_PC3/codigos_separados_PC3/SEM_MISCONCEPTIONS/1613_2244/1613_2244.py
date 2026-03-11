from numpy import*
v= array(eval("v:"))
t= array(eval("t:"))
i= 0
while(i<size(v)):
	if(v[i]=="ALONGAMENTO"):
		i= i+1
	elif(v[i]=="CORRIDA"):
		i= i+1
	elif(v[i]=="DANCA"):
		i= i+1
	elif(v[i]=="ESCALADA"):
		i= i+1
	elif(v[i]=="HIDROGINASTICA"):

print(round(i,2))