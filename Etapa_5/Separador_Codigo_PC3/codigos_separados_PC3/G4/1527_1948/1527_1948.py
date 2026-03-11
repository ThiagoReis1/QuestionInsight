#--------------------------------------------------
#Universidade Federal do Amazonas
#Larisse Gabriele Ramos de Abreu
#Data: 21/12/2016
#
#Objetivo: Cedulas
#---------------------------------------------------

A = int(input("Quantidade de seguidores do deus Forseti: "))
B = int(input("Quantidade de seguidores do deus Loki: "))
a = float(input("O percentual anual dos seguidores do deus Forseti: "))
b = float(input("O percentual anul dos seguidores do deus Loki: "))

aa = a/100
bb = b/100

vA = A
vB = B

anos = 0
while(vA > vB):	
	vA = vA + vA * aa
	vB = vB + vB * bb
	anos = anos + 1
print(anos)