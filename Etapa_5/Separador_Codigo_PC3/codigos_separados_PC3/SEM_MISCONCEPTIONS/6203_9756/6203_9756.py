altura_macaco = 1.4
taxa_macaco = 0.06
alt_leao = float(input("Digite a altura do leao: "))
tx_cresc = float(input("Digite a taxa de crescimento do leao: "))

macaco = altura_macaco + taxa_macaco
leao = alt_leao + tx_cresc

contador = 0

while macaco < leao:
	contador = contador + 1
	
print (contador)