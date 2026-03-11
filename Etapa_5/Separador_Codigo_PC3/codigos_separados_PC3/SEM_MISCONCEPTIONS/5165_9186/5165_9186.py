# o peso do saco de racao
peso_do_saco = float(input( " digite o peso do saco de racao: "))
# a quantidade diaria de racao
quantidade_diaria = float(input( " digite a quantidade diaria de racao: "))
# a quantidade de racao que restara no saco apos 6 dias
quantidade_apos_6_dias = peso_do_saco - quantidade_diaria * 6
# resultado
print(round(quantidade_apos_6_dias, 4))