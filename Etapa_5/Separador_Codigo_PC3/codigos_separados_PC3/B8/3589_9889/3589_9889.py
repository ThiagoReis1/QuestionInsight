from numpy import *

aneis = array(eval(input("Digite os vetores de aneis: ")))

pj = 0 #pontuacao do jogador
anel = array([1,2,3,4])

for anel in aneis:
	if (anel == 1):
		pj = pj + 80
		
	elif (anel == 2):
		pj = pj + 40
		
	elif (anel == 3):
		pj = pj + 20
		
	elif (anel == 4):
		pj = pj + 10
		
print(pj)