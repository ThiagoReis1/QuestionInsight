v1= float(input("notas:"))
v2= float(input("notas:"))
v3= float(input("notas:"))
v4= float(input("notas:"))
v5= float(input("notas:"))

media = (v1+v2+v3+v4+v5) / 5

if (media >= 5):
   mens = ("Aprovado")
else:
   mens = ("Reprovado")

print(round(media, 1))
print(mens)

