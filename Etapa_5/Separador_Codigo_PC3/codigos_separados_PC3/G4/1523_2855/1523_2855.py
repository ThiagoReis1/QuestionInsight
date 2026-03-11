Qi = int(input("Quantidade inial de balões: "))
Qc = int(input("Quantidade de balões costruidos: "))
Qd = int(input("Quantidades de balões detruidos: "))

sem = 0
Qt = Qi +(Qc -Qd)*0
while(Qt < 200):
	sem = sem + 1
	Qt = Qi + (Qc - Qd)*sem
print(sem)