#Universidade Federal do Amazonas
#Thiago Tuma Camilo 21600549

lam = int(input("Digite a população inicial de lambaris:"))
tuc = int(input("Digite a população inicial de tucunarés:"))
taxlam = float(input("Digite a taxa mensal de crescimento do número de lambaris(%):"))
taxtuc = float(input("Digite a taxa mensal de crescimento do número de tucunarés(%):"))

meses = 0
t = tuc
l = lam
while (l > t):
	l = l + (l * (taxlam/100)) - (2 * t)
	t = t + (t * (taxtuc/100))
	meses = meses + 1
	
print(meses)