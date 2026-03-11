aluguel = 50.00
taxa = 30.00


dias = int(input("digite o valor de dias do aluguel:"))
total = dias * aluguel + taxa
total2 = total * 1.18

print(round(total2, 2))