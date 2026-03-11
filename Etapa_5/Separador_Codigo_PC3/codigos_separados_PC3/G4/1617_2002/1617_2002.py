from numpy import *

sword = array(eval(input("Tipos de Espadas: ").upper()))
lv  = array(eval(input("Níveis dos combatentes: ")))
i = 0
dmg = 0
#dmg = dano espada * nível
while i < size(sword):
	if sword[i] == "CENOURA":
		dmg = dmg + 2*lv[i]
	if sword[i] == "FERRO":
		dmg = dmg + 4*lv[i]
	if sword[i] == "DWARVEN":
		dmg = dmg + 8*lv[i]
	if sword[i] == "ELVEN":
		dmg = dmg + 11*lv[i]
	if sword[i] == "DAEDRIC":
		dmg = dmg + 14*lv[i]
	i = i + 1
	
print(dmg)