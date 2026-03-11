peso = float(input("Qual o peso?"))
quantidade = float(input("Qual a quantidade de racao diaria em gramas?"))

racao = quantidade * 7
racao2= peso - racao
print(round(racao2,2))
