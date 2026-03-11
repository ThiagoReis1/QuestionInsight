B= float(input("Digite o valor da base maior em metros: "))
b= float(input("Digite o valor da base menor em metros: "))
h= float(input("Digite o valor da altura em metros: "))
custo= float(input("Digite o custo do fertilizante por metros quadrados: "))

area= h*(B+b)/2

total=area*custo

print(round(total,2))

