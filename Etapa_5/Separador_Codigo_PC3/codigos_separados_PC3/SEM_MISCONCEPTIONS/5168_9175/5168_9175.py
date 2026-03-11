peso_do_saco = float(input("digite o peso do saco: "))
quantidade_de_racao = float(input("digite a quantidade de racao: "))
quantidade_apos_7_dias = peso_do_saco - quantidade_de_racao * 7
print(round(quantidade_apos_7_dias, 4))