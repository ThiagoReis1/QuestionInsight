qm=int(input("quantidade de mana: "))
qg=int(input("quantidade de mana gasta por dia: "))
qr=int(input("quantidade de mana recuperada por noite: "))

t=1

while(qm<=0):
	qm=qm+qr-qg
	t=t+1
print(t)