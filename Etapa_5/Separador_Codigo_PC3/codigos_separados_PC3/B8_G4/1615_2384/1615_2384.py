from numpy import *

v1 = array(eval(input("v1: ")))
v2 = array(eval(input("v2: ")))
s1 = 0
s2 = 0
i = 0

while(i<size(v1) and i<size(v2)):
	if(v1[i]==1):
		s1=s1+40
	elif(v1[i]==2):
		s1=s1+20
	elif(v1[i]==3):
		s1=s1+10
	if(v2[i]==1):
		s2=s2+40
	elif(v2[i]==2):
		s2=s2+20
	elif(v2[i]==3):
		s2=s2+10
	i=i+1
	
if(s1>s2):
	print("JOGADOR UM")
elif(s2>s1):
	print("JOGADOR DOIS")
else:
	print("EMPATE")

