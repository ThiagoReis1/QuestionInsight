peso_do_saco = float(input("Insira o Peso da Racao: "))
quant_de_racao = float(input("Insira a Quantidade Diaria de Racao: "))
t = 7

quant_final = peso_do_saco - quant_de_racao * t

print(round(quant_final, 4))