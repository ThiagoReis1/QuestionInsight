ent1 = input("")
ent2 = int(input(""))
ent3 = int(input(""))
ent4 = int(input(""))

if(ent1 == "sabre"): 
	dano = (ent3+ent4)+(2*ent2)
	print(dano)
else:
	dano = (2*(ent3+ent4))+ent2
	print(dano)