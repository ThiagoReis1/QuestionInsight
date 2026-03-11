peso = float(input("Peso do saco de racao: "))

quantidade = float(input("Quantidade diaria de racao: "))

rquantidade = peso - (quantidade*7)

print(round(rquantidade,4))