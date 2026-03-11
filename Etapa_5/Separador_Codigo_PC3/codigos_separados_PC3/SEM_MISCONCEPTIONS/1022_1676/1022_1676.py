#Lunna Maria Braga Souza -21553780

a = 8
area = (2 * a **2 * (2**0.5 + 1))
comprimento = float(input("qual é o comprimento?"))
custo_m2 = float(input("quanto é o custo?"))
custo_total = (area * custo_m2 + comprimento)
print(round(custo_total,2)