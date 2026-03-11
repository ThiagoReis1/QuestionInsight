#Adriano Crelli de Brito - 121555121
#UFAM
#AV1- Q001



basemaior = float(input("Digite a base: "))
basemenor = float(input("Digite a base: "))
alt = float(input("Digite a altura:"))
custo = float(input("Digite o custo:"))

area = alt * (basemaior + basemenor) / 2
custototal = custo * area

print(round(custototal, 2))