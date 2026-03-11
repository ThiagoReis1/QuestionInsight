a = int(input("ano de nascimento:"))
p = input("pais:"). upper()
d = 2023 - a

if p == "B":
   if d > 21:
      print("sim")
      x = d - 21
      print(x)
   else:
      print("nao")
      x = 21 - d
      print(x)
elif p == "C":
   if d >24:
      print("sim")
      x = d - 24
      print(x)
   else:
      print("nao")
      x = 24 - d
      print(x)
else:
     print(invalido)