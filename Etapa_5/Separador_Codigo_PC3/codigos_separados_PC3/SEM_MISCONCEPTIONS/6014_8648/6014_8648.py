#Variáveis de entrada:
valor_da_renda = float(input("Digite o valor da renda: "))
valor_da_prestacao = float(input("Digite o valor da prestacao: "))
#Condições e cálculo:
if (valor_da_renda * 0.35 > valor_da_prestacao):
 print("Emprestimo aprovado")
else:
 print("Emprestimo nao aprovado")