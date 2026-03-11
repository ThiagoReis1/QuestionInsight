alturaeu = float(input("Qual a sua altura? "))
alturaamg = float(input("Qual a altura do seu amigo?"))

#Saber quem é o mais alto
if (alturaeu > alturaamg):
	malt = alturaeu
	
else: 
	malt = alturaamg

#Saber a permissão (se sim ou não)
if (alturaeu < 1.37 and alturaamg < 1.37):
	perm = ("Nao")
	
else:
	perm = ("Sim")
	
print(perm)
print(malt)