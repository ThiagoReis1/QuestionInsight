from math import*
bm = float(input("base maior"))
b = float(input("base menor"))
h = float(input("altura"))
custo = float(input("custo total"))

area = (h*(bm+b))/2
custot = area*custo
print(round(area*custo,2))
