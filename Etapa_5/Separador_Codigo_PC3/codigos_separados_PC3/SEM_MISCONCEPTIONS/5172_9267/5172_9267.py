peso = float(input("Digite o peso do saco de racao em gramas:"))
quantidade = float(input("digite a quantidade de racao em gramas:"))
quantidadeDeRacao = (peso - quantidade * 5)
print(round(quantidadeDeRacao,2))
