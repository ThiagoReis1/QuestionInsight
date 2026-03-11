B=float(input("digite o B: "))
b=float(input("digite o b: "))
h=float(input("digite h: "))
custo_m2= float(input("digite o custo: "))

area= h*(B+b)/2

custo_total=(area*custo_m2)

print(round(custo_total, 2))