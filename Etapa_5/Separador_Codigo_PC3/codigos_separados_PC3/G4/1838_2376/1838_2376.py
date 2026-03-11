#Resistor 1
r_1 = float(input("Insira o valor do resistor 1:"))

#Resistor 2
r_2 = float(input("Insira o valor do resistor 2:"))

#Resistor 3
r_3 = float(input("Insira o valor do resistor 3:"))

#Resistencia equivalente
R = (r_1 * r_2 * r_3) / ((r_1 * r_2) + (r_2 * r_3) + (r_1 * r_3))

#Impressao da resistencia equivalente
print(R)