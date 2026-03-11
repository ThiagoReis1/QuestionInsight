qif = int(input("seguidores de Forseti: "))
qil = int(input("seguidores de Loki: "))
crescf = float(input("prcentual de crescimeneto de Forseti: "))
crescl = float(input("prcentual de crescimeneto de Loki: "))

anos = 0

while (qif > qil):
	qif = qif + (qif * crescf)/100
	qil = qil + (qil * crescl)/100
	anos = anos + 1
print(anos)