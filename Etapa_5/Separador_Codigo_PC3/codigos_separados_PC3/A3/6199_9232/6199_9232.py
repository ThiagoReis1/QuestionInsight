altura_cicero = 1.8
taxa_cicero = 0.01
anos = 0

altura = float(input("altura: "))
taxa_cresc = float(input("taxa de crescimento: "))

# na aba dicas, diz "considere que a taxa de crescimento do aluno NUNCA será maior que a de cicero" (terceiro ponto), mas em
# todos os exemplos de entrada na aba logo abaixo incluem taxas de crescimento maiores do que a dele. o certo seria o programa
# dar invalido? ou nao... nao entendi bem essa questao.

while altura < altura_cicero:
	altura_cicero += 0.01
	altura += taxa_cresc
	anos += 1
print(anos)