valor = float(input("Determine o valor a ser pago:"))
gasolina = 2.86
servico_de_troca = 50.00
imc = 34 / 100
valor_total = (gasolina + servico_de_troca)

print(round(valor_total * imc, 2))