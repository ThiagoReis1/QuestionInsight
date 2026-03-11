peso= float(input("Peso do saco de racao:"))
diaria= float(input("Insira a quantidade diaria:"))

c1= diaria * 7
c2= peso - c1

print(round(c2, 3))