valor_renda = float(input('qual sua renda: '))
prestacao_mensal = float(input('valor da prestacao: '))

limite_20pp = valor_renda * .2

if prestacao_mensal > limite_20pp:
  print('Emprestimo nao aprovado')
else:
  print('Emprestimo aprovado')