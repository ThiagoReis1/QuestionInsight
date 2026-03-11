valor_renda = float( input('Insira o valor da renda'))
valor_prestacao = float(input('insira o valor da prestacao'))

porcentagem = (valor_renda * 30 / 100)

if valor_prestacao > porcentagem:
   print('Emprestimo nao aprovado')
else:
   print('Emprestimo aprovado')