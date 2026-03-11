altura_macaco = 1.4
taxa_macaco = 0.06
altura_leao = float(input("altura do leao:"))
taxa_leao = float(input("taxa do leao:"))
anos = 0

while altura_macaco <= altura_leao:
	if taxa_leao<taxa_macaco:
		altura_macaco += taxa_macaco
		altura_leao += taxa_leao
		anos+=1

print(anos)
