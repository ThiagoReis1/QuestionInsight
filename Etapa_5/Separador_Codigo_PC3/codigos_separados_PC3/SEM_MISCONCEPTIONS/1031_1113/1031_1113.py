quantidade_litros = float(input("Qual a quantidade em litros de gasolina?"))
preco_gasolina = 2.86
servico_troca = 50
ICMS = 34/100
p = preco_gasolina * quantidade_litros + servico_troca
p1 = p * ICMS
custo_total = p1 + p
print(round(custo_total, 2))
