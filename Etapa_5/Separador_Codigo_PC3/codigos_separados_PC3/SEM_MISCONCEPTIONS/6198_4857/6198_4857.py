altura_luna = 1.65
taxa_luna = 0.02

ap = float(input("Digite sua altura: "))
tp = float(input("Digite sua taxa de crescimento: "))

ac = 0
while (ap < altura_luna):
	ap= ap +tp
	altura_luna = altura_luna+taxa_luna
	ac= ac+1
print(ac)
	
