carros = float(input("digite a quantidade de carros: "))
basemaior = float(input("digite a base maior: "))
basemenor = float(input("digite a base menor: "))
altura = float(input("digite a altura: "))
area = (altura * (basemaior + basemenor))/2
total = carros * area
print(round(total,2))