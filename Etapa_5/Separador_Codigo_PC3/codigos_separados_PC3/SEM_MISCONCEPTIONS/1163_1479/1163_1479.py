lam = int(input("Digite a população inicial de lambaris: "))
tuc = int(input("Digite a população inicial de tucunaré: "))
taxlam = float(input("Digite a taxa mensal dos lambaris: "))
taxtuc = float(input("Digite a taxa mensal dos tucunarés: "))

meses = 0
t = tuc
l = lam
while (l > t):
	l = l + (l * (taxlam/100)) - (2 * t)
	t = t + (t * (taxtuc/100))
	meses = meses + 1
print(meses)