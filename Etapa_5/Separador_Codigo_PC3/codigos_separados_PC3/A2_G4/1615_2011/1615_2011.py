from numpy import *

jog1 = array(eval(input("  jog1 :  ")))
jog2 = array(eval(input("  jog2 :  ")))

p1=0
i=0
while (i < size(jog1)):
	if(jog1[i] == 1):
		p1=p1+40
		i=i+1
	elif(jog1[i] == 2):
		p1=p1+20
		i=i+1
	elif(jog1[i] == 3):
		p1=p1+10
		i=i+1
	else:
		p1=p1
		i=i+1
p2=0
i=0
while (i < size(jog2)):
	if(jog2[i] == 1):
		p2=p2+40
		i=i+1
	elif(jog2[i] == 2):
		p2=p2+20
		i=i+1
	elif(jog2[i] == 3):
		p2=p2+10
		i=i+1
	else:
		p2=p2
		i=i+1
		
if (p1 > p2):
	print("JOGADOR UM")
elif(p2 > p1):
	print("JOGADOR DOIS")
else:
	print("EMPATE")