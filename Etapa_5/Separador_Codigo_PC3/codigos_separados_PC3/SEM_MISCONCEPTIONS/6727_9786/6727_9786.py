num = int(input('Digite um numero:'))
quo = (num // 31)
resto = (num % 31)

if (num % 31 == 0):
   mensagem = 'sim'
   print(quo)
   print(mensagem)
else:
   mensagem = 'nao'
   print(resto)
   print(mensagem)