#Universidade Federal do Amazonas
#Instituto de Computacao-UFAM
#Departamento:Fisica
#Disciplina:Introducao a Programacao de Computadores(IPC20161)
#Professor:Mario Salvatierra Junior
#Aluno:Frank Lucas Duarte Ozorio
#Numero de matricula:21553797
#Objetivo:Escreever um script em Python na qual dado a medida do preco por litro,servico de troca de oleo e o ICMS,determinar um programa que leia a quantidade de litros abastecidos e determine o valor a ser pago.

#Descricao de variaveis:
#preco_por_litro ----------------preco por litro de gasolina]
#servico_troca_oleo--------------servico de troca de oleo
#imposto_CMS-------------------- imposto sobre circulacao de mercadorias e servicos
#quantidade_de_litros---------- quantidade de litros abastecidos
#custo_total-------------------- custo total do servico

#Quantidade de litros abastecidos
quantidade_de_litros=float(input("Quantidade de litros:"))

preco_por_litro= 2.86 * quantidade_de_litros

servico_troca_oleo= 50.00

#Imposto ICMS:
imposto_CMS= (preco_por_litro + servico_troca_oleo) * 0.34

#Custo total do servico:
custo_total= preco_por_litro + servico_troca_oleo + imposto_CMS

print(round(custo_total,2))


