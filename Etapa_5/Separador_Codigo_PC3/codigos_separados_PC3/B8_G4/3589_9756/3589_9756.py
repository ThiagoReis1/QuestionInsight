from numpy import *
vnum = array(eval(input("Informe os numeros dos vetores: ")))
i = 0
pts1 = 0
pts2 = 0
pts3 = 0
pts4 = 0

while i < size(vnum):
	if vnum[i] == 1:
		pts1 = pts1 + 1
	elif vnum[i] == 2:
		pts2 = pts2 + 1
	elif vnum[i] == 3:
		pts3 = pts3 + 1 
	elif vnum[i] == 4:
		pts4 = pts4 + 1
	i = i + 1
ptst = ((pts1*80)+(pts2*40)+(pts3*20)+(pts4*10))

print (ptst)