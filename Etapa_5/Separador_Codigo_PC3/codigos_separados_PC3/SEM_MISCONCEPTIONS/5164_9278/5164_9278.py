peso = float(input("Peso do saco em gramas: "))
qtd = float(input("Quantidade diaria em gramas: "))

qtd_restante = peso - (qtd*4) 

print(round(qtd_restante,2))