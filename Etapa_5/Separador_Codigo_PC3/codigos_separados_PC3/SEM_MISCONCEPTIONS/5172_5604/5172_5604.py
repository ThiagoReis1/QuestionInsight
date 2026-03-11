peso= float(input("digite peso do saco de racao: "))
quant= float(input("dose diaria de racao: "))

racao= quant * 5
restante = peso - racao

print(round(restante, 2))
