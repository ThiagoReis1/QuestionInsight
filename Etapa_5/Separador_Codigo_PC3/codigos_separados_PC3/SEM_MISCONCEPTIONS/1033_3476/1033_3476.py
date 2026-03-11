peso = float(input("Digite um numero: "))
frete = (peso * 43.21) + 25.00 
CT = (frete * 62/100) + frete
print(round(CT,1))