mo = int(input("moedas de ouro: "))
dm = int(input("despesa mensal: "))
ip = int(input("imposto mes: "))
rb = int(input("moedas roubadas: "))

i = 0
s = 0

while(mo>0):
	mo = mo + ip - (dm + rb)
	i += 1

print(i)