peso = float( input() )
qtd_racao = float( input() )

qtd_resto = peso - (qtd_racao * 6)

print(round(qtd_resto, 4))