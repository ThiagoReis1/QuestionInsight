n = int(input("numero:  "))
a = n%17

if a == 0:
   b = n//17
   print(b)
   mensagem = "sim"
   print(mensagem)
else:
   print(a)
   mensagem = "nao"
   print(mensagem)