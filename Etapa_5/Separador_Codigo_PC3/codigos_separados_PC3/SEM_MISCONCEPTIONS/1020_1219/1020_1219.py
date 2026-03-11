B =float(input("Base maior:"))
b =float(input("Base menor:"))
h =float(input("Altura:"))
custo =float(input("Custo aplicaçao:"))
area = h*(B+b)/2
custo_total = area*custo
print(round(custo_total,2))