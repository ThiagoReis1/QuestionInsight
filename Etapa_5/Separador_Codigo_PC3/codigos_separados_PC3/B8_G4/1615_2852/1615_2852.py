from numpy import*
p1 = array(eval(input()))
p2 = array(eval(input()))

a = size(p1)
k = size(p2)
pp1 = 0
pp2 = 0
b = 0
while(a>b):
	a = a - 1
	if(p1[a]==1):
		pp1 = pp1 + 40
	elif(p1[a]==2):
		pp1 = pp1 + 20
	elif(p1[a]==3):
		pp1 = pp1 + 10
	elif(p1[a]==4):
		pp1 = pp1 + 0
while(k>b):
	k = k - 1
	if(p2[k]==1):
		pp2 = pp2 + 40
	elif(p2[k]==2):
		pp2 = pp2 + 20
	elif(p2[k]==3):
		pp2 = pp2 + 10
	elif(p2[k]==4):
		pp2 = pp2 + 0

if(pp1>pp2):
	print("JOGADOR UM")
elif(pp1<pp2):
	print("JOGADOR DOIS")
elif(pp1==pp1):
	print("EMPATE")