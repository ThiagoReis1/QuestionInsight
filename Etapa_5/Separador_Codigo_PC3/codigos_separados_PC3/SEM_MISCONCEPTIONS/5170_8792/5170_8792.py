peso = float(input("O peso do saco de racao: "))
qdd = float(input("A quantidade diaria de racao: "))

conta = (qdd * 7)
conta2 = (peso - conta)

print(round(conta2, 3))