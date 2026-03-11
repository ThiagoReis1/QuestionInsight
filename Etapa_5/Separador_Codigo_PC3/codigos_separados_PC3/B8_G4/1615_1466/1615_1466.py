from numpy import *
a=array(eval(input())).astype(dtype=int)
b=array(eval(input())).astype(dtype=int)
i=0
s1=0
s2=0
while(i<size(a)):
	if(a[i]==1):
		s1+=40
	elif(a[i]==2):
		s1+=20
	elif(a[i]==3):
		s1+=10
	if(b[i]==1):
		s2+=40
	elif(b[i]==2):
		s2+=20
	elif(b[i]==3):
		s2+=10		
	i+=1
if(s1>s2):
	print("JOGADOR UM")
elif(s2>s1):
	print("JOGADOR DOIS")
else:
	print("EMPATE")