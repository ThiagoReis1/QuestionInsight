sn = float(input("digite a quantidade: "))
sais = float(input("digite a quantidade: "))
amanita = float(input("digite a quantidade: "))

porcao_sn = int(sn/0.3)
porcao_sais = int( sais/0.73)
porcao_amanita =int(amanita/2.64)

print(min(porcao_sn, porcao_sais, porcao_amanita))

