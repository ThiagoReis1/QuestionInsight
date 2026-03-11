B = float(input("digite o comprimento da base maior: "))
b = float(input("digite o comprimento da base menor: "))
h = float(input("digite a altura do trapezio: "))
custo = float(input("digite o custo de aplicação do fertilizante por metro quadrado: "))

area = (h*(B+b)) /2
				 
total = custo*area

print(round(total, 2))