peso = float(input("o peso do saco de racao: "))
quantidade = float(input("a quantidade diaria da racao em dias: "))

total = peso-(quantidade*7)

print(round(total,2))
