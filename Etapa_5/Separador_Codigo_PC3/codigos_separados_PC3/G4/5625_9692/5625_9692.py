x = input("T ou S: ")
qntd = int(input("insira o numero: "))
acai = int(input("insira o numero: "))
if x == 'S':
	total = (qntd*4)+(acai*10)
else:
	total = (qntd*5.50)+(acai*10)
print(total)
    