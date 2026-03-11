saco_racao = float(input("peso do saco em gramas:"))
qnt_dia = float(input("quantidade diaria de racao em gramas:"))

restante = saco_racao - (qnt_dia*7)

print(round(restante,2))