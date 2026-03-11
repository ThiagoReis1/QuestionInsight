peso = float(input("Qual o peso do saco de racao: "))
quantidade = float(input("Qual a quantidade diaria de racoes em grama fornecidas:?"))	  

quantidade_total = (quantidade*7) - (peso)
print(abs(round(quantidade_total, 2)))



