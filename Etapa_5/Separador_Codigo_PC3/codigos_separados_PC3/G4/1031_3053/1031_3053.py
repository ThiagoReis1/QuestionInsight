qtd = float(input("quantidade de litros: "))
p = 2.86
t = 50.00
P = qtd*p
T = P + t
B = ((T*134)/100)
print(round(B , 2))