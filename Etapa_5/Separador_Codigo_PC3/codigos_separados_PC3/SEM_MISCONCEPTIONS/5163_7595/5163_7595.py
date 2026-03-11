peso_racao = float(input("Insira o peso do saco de racao: "))
quant_racao = float(input("Insira a quantidade diaria de racao: "))

quant_cinco_dias = quant_racao * 5
peso_racao_att = peso_racao - quant_cinco_dias

print(round(peso_racao_att,3))