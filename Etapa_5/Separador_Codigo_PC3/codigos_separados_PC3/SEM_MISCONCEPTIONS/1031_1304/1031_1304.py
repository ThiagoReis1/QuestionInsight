#Lucas de Sousa Martins
#16/06/2016
litros_gasolina = float(input("Insira a quantidade de litros de gasolina: "))
troca_oleo = 50.0
preco_gasolina = litros_gasolina * 2.86
total = preco_gasolina + troca_oleo
ntotal = 0.34 * total + total
print(round(ntotal,2))