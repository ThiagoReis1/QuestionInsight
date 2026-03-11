a = float(input("nota 1"))
b = float(input("nota 2"))
c = float(input("nota 3"))
d = (a + b + c) / 3
print(round(d,1))
if(d >= 5):
   mensagem = "Aprovado"
else:
   mensagem = "Reprovado"
print(mensagem)