a = float(input("nota 1 = "))
b = float(input("nota 2 = "))
c = float(input("nota 3 = "))
media = round((a + b + c)/3,1)
print(media)
if media > 5 :
	print("Aprovado")
elif media == 5 :
	print("Aprovado")
else :
	print("Reprovado")