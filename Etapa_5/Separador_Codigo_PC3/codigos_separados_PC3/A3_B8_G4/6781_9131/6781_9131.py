ano = int(input("ano de nascimento: "))
pais = input("B ou E? ").upper()
idade = 2023 - ano
sim = "sim"
nao = "nao"
if pais == "B":
   idade >= 21
   print(nao)
   ap = 21 - idade
   print(ap)
elif pais == "B":
   idade < 21
   print(sim)
   p = idade - 21	
   print(ap)
elif pais == "E":
   idade >= 18
   print(sim)
   ap = idade - 18
   print(ap)
elif pais == "E":
   idade < 18
   print(nao)
   ap = 18 - idade
   print(ap)
elif pais != "B" or "E":
   mensagem = "invalido"
   print(mensagem)