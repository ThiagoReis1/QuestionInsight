# Universidade Federal do Amazonas
# Aluno: Nelson Geraldo
# Curso: Estatistica

# Inputs ( peso do saco de racao em gramas, qtd diaria de racao em gramas )
peso_racao = float(input('Digite o peso do saco de racao (g): '))
qtde_diaria = float(input('Digite a quantidade diaria de racao (g): '))

# Calculando o que restara apos uma semana
resultado = peso_racao - (qtde_diaria * 7)

# Outputs ( qtd de racao em gramas que restara no saco apos uma semana ) - arrendondar para quatro casas decimais
print(round(resultado, 4))