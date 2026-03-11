a=int(input("Digite o valor do resistor 1: "))
b=int(input("Digite o valor do resistor 2: "))
c=int(input("Digite o valor do resistor 3: "))

req = (a*b*c) / ((a*b) + (b*c) + (a*c))

print(req)