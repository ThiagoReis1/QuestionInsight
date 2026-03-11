from numpy import*

j1 = array(eval(input("Aneis do jogador 1: ")))
j2 = array(eval(input("Aneis do jogador 2: ")))

i=0
y=0
x=0
while i<size(j1):
	if j1[i]==1:
		m=40
		y=y+m
	if j1[i]==2:
		a=20
		y=y+a
	if j1[i]==3:
		r=10
		y=y+r
	if j1[i]>=4:
		c=0
		y=y+c
	if j2[i]==1:
		m=40
		x=x+m
	if j2[i]==2:
		a=20
		x=x+a
	if j2[i]==3:
		r=10
		x=x+r
	if j2[i]>=4:
		c=0
		x=x+c	
	i=i+1
if x>y:
	print("JOGADOR DOIS")
if y>x:
	print("JOGADOR UM")
if y==x:
	print("EMPATE")
		
