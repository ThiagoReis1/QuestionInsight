saco_peso = float(input("Digite o peso do saco: "))
qtde_racao = float(input("Digite a quantidade de racao diaria: "))

qtde_restante = saco_peso - (qtde_racao * 7)

print (round(qtde_restante , 4))
