from numpy import*

notas = array(eval(input("Digite as notas: ")), dtype = float)
qtd_notas = int(size(notas)) 
i = 0
nota_menor = min(notas)

media_final = (sum(notas) - nota_menor)/3.0
print(round(media_final, 2))

if(media_final >= 5.0):
	print("APROVOU")
else:
	print("REPROVOU")

