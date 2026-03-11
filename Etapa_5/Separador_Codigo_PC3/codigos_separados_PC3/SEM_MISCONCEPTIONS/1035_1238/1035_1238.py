# Talita Oliveira Gomes Passos
# Matricula: 21552161
# 16 de Junho de 2016
# Exercicio 2 da avaliacao

# Quantidade em reais que o cliente dara
reais = float(input("Digite o valor em reais: "))

# Quantidade em reais que o cliente dara menos a taxa fixa 
troca_para_euros = ( reais - 15 )

# Quantidade em euros que o cliente recebera
euros = troca_para_euros / 3.96

print(round(euros, 2))