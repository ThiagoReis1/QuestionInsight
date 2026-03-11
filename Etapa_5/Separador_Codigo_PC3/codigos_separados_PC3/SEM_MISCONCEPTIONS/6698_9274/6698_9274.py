qtd_praca =  int(input("Qual a quantidade de pracas de pedagio?"))

valor_pago = qtd_praca * 9.8 + 20

valor_c_taxa = valor_pago + valor_pago *(15/100)

print(round(valor_c_taxa,2))