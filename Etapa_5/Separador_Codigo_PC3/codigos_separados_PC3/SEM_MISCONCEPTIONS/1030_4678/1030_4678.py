min_exc = float(input("Quantidade de minutos excedentes consumidos durante o mes: "))
min_total = min_exc*0.97
min_plano = 45 + min_total
ICMS = ((45 + min_total)/100)*42
valor_conta = min_plano + ICMS
print(round(valor_conta, 2))