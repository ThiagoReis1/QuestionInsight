#R = variável do resistor.

r1 = int(input("Digite o valor do resistor: "))
r2 = int(input("Digite o valor do resistor: "))
r3 = int(input("Digite o valor do resistor: "))

#Req = Resistência equivalente.

Req = (r1 * r2 * r3)/((r1 * r2) + (r2 * r3) + (r1 * r3))

print(Req)