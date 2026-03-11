peso = float(input("digite um num: "))
quant_diaria = float(input("digite um num: "))

quantidade_racao = peso - (quant_diaria * 4)
print(round(quantidade_racao,2))