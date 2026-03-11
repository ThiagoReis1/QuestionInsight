qi = int(input("quantidade inicial de balões na frota do rei Gardoc:"))
qc = int(input("quantidade C de novos balões construídos:"))
qd = int(input("quantidade D de balões destruídos pelos djinns: "))

sem = 0;
cont = qi;

while(cont < 200):

	cont += qc;
	cont -= qd;
	sem += 1; 

	
print(sem)
