altura_joe = 1.77
taxa_joe = 0.02
#Variável contadora:
ano = 0
#Variáveis de Leitura
altura_pessoa = float(input("Digite sua altura: "))
taxa_pessoa = float(input("Digite sua taxa de crescimento: "))
#Condição repetição:
while (altura_pessoa > altura_joe):
      if (taxa_pessoa < taxa_joe):
        altura_pessoa += (1 - taxa_pessoa)
        altura_joe += (1 - taxa_joe)
        ano = ano + 1
print(ano)