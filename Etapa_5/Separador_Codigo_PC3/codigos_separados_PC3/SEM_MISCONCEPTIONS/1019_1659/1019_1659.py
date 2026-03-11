# Leandra de Souza Mendes - Matricula 21554018
# Data 16 / 06 / 2016

largura = float(input("Digite a largura da fazenda: "))
comprimento = float(input("Digite o comprimento da fazenda em metros: "))
custo_funcio = float(input("Digite o custo de aplicacao do fungicida"))

custo_total_servico = largura * comprimento * custo_funcio 

#Arredondar o valor em duas casas decimais
#para representar os centavos

print(round(custo_total_servico, 2))