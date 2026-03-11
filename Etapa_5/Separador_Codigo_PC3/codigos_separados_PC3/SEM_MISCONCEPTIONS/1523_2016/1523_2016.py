i = int(input("A quantidade inicial de balões na frota do rei Gardoc: "))
c = int(input("A quantidade e novos balões construídos por semana: "))
d = int(input("A quantidade destruídos pelos djinns a cada semana: "))
semana = 0
total = i
while (total<200):
	total = total+c-d
	semana = semana+1
print(semana)