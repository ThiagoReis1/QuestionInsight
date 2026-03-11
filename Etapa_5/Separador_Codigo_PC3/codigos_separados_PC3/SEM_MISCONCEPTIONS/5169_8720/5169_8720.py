peso=float(input("Peso do saco de racao:"))
qdia=float(input("Quantidade diaria de racao:"))
qrest=peso-(4*qdia)
print(round(qrest, 2))