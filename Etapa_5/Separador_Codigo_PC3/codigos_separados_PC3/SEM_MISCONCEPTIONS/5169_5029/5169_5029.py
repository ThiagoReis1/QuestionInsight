peso_saco = float(input("Peso do saco de racao: "))
qt_racao = float(input("Quantidade diaria de racao: "))
resto_racao = peso_saco-(qt_racao*4)
print(round(resto_racao,2))