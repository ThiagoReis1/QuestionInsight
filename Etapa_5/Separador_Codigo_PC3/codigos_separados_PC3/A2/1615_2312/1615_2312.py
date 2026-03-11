from numpy import *
anel1=array(eval(input("vetor 1")))
anel2=array(eval(input("vetor 2")))
u=0
soma1=0
soma2=0
while u<len(anel1):	
	if int(anel1[0])==1:
		soma1=soma1+40
	if int(anel1[0])==2:
		soma1=soma1+20
	if int(anel1[0])==3:
		soma1=soma1+10
	else:
		soma1=soma1
	u=u+1
o=0
while o<len(anel2):	
	if int(anel2[0])==1:
		soma2=soma2+40
	if int(anel2[0])==2:
		soma2=soma2+20
	if int(anel2[0])==3:
		soma2=soma2+10
	else:
		soma2=soma2+0
	o=o+1
if soma1>soma2:
	print("JOGADOR UM")
if soma2<soma1:
	print("JOGADOR DOIS")
if soma1==soma2:
	print("EMPATE")
