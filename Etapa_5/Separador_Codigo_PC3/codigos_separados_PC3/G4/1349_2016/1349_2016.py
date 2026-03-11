var = float(input("Digite a estimetiva de arvores por m²: "))
a = float(input("Digite o comprimento do lado da regiao: "))
area = (a**2*(25+10*5**0.5)**0.5)/4
valor = var*area
print(round(valor,0))