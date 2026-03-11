habitantesH = float(input("Numero de habitantes: "))
vampirosV = float(input("Numero de vampiros: "))
tranformacoes_diaX = float(input("Numero de tranformacoes: "))
morte_diaY = float(input("Numero de vampiros mortos: "))
t = 0
soma=0
while(habitantesH <= 0):
	habitantesH = vampirosV/(transformacoes_diaX*habitantesH)
	soma= vampirosV/morte_diaY 
	t = t + 1
	print(t)