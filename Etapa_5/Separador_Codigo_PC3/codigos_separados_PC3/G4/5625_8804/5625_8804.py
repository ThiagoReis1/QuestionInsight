tipo = input("T tapioca ou S salgado: ")
qnt = int(input("Quantidade: "))
qnt_a = int(input("Quantidade de acais"))

if tipo == 'T':
	t = (qnt*5.50)+ (10*qnt_a)
else:
	t = (4*qnt) + (10*qnt_a)
print(round(t,1))