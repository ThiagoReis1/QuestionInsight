a = (float(input(" digitar nota a,2 ")))
b = (float(input(" digitar nota b,2 ")))
c = (float(input(" digitar nota c,2 ")))
d = (float(input(" digitar nota d,2 ")))

mediaari = a+b+c+d
mediafinal = mediaari/4
if (mediafinal >= 7):
	print(round(mediafinal, 2))
	print("Aprovado")
else :
	print(round(mediafinal, 2))
	print("Reprovado")