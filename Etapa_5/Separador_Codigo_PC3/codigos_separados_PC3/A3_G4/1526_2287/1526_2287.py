qom=int(input("quantidade inicial de manas:"))
qm=int(input("quantidade de manas que gasto no dia:"))
qr=int(input("quantidade de manas que recupera por noite:"))
t=0

while(qom>0):
	qom= (qom-qm) + qr
	saldo= qom 
	t= t + 1 
print(t)
	
	