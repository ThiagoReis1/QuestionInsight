peso= float(input("peso do saco em gramas: "))
quantidade= float(input("quantidade diaria de ração: "))
diaria= peso-(quantidade*4)
total= diaria*4/4
print(round(total, 2))