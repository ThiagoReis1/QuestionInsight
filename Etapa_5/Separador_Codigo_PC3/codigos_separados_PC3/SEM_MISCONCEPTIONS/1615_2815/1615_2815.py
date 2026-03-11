from numpy import *
a= array(eval(input("Vetor: ")))
b= array(eval(input("Vetor: ")))
i=0
i1=0
primeiro=0
segundo=0
while(i<size(a)):
	if(a[i]==1):
		primeiro=primeiro+40
		i=i+1
	elif(a[i]==2):
		primeiro=primeiro+20
		i=i+1
	elif(a[i]==3):
		primeiro=primeiro+10
		i=i+1
	else:
		primeiro=primeiro+0
		i=i+1
while(i1<size(b)):
	if(b[i1]==1):
		segundo=segundo+40
		i1=i1+1
	elif(b[i1]==2):
		segundo=segundo+20
		i1=i1+1
	elif(b[i1]==3):
		segundo=segundo+10
		i1=i1+1
	else:
		segundo=segundo+0
		i1=i1+1	
		
if(primeiro>segundo):
	print("JOGADOR UM")
elif(segundo>primeiro):
	print("JOGADOR DOIS")
else:
	print("EMPATE")
		
