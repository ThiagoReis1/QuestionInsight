#Karen Hanna Schoaba - 21600523
#Avaliacao 01 - Ex 01
#16/06/2016

basemaior=float(input("Digite base maior"))
basemenor=float(input("Digite base menor"))
altura=float(input("Digite altura"))
custoappfert=float(input("Aplicação por metro quadrado"))

area=altura*(basemaior+basemenor)/2
custototal=area*custoappfert

print(round(custototal, 2))