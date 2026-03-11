from numpy import *

v1=input("Digite o tipo de espada: ")
v2=array(eval(input("Digite o nivel do combatente: "))) #nivel do combatente


elif(v1[0:]=="CENOURA") 
	dano1=2*v2[0]
elif (v1[0:]=="FERRO"):
	dano2=4*v2[1]
elif (v1[0:]=="DWARVEN"):
	dano3=8*v2[2]
elif (v1[0:]=="ELVEN"):
	dano4=11*v2[3]
elif (v1[0:]=="DAEDRIC"):
	dano5=14*v2[4]

danototal=dano1+dano2+dano3+dano4+dano5
print(danototal)