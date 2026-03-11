valor_da_encomenda= float(input("Qual o valor da encomenda? "))

imposto= valor_da_encomenda * (81/100) + 12.00
valor_final= valor_da_encomenda + imposto

print(round(valor_final, 2))