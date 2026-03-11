#Universidade Federal do Amazonas
#Curso de engenharia de produção
#Matéria: Introdução a ciancia dos computadores
#Aluno: Allan Bezerra - 21552438

valor = float(input("Quantia a ser convertida R$: "))
#Calculos
taxa_de_servico = 8.50
valor_a_ser_convertido = valor - taxa_de_servico
#convercao
cotacao_iene = 0.03
convercao = valor_a_ser_convertido / cotacao_iene
print(round(convercao,2))