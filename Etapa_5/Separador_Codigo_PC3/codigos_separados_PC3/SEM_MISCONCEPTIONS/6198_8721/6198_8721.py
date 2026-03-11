alturaluna = 1.65
taxaluna = 0.02
a = float(input("Digite a altura :"))
t = float(input("Digite a taxa: "))
an = 0
while a < alturaluna:
	a = a + t
	alturaluna = alturaluna + taxaluna
	an = an + 1
print (an)
