consumo = float(input("digite um valor: "))
valor_fixo = 23
taxa_pormin = 0.28
icms = 31 / 100
valor_pagar = (consumo * taxa_pormin + valor_fixo) + (consumo * taxa_pormin + valor_fixo) * icms
print(round(valor_pagar, 2))
