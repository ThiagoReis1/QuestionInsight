ingred = input()
quanti = int(input())
if(ingred.lower() == "arroz" and quanti > 0 and quanti < 10000):
	receitas = quanti // 500
	print(receitas)
elif(ingred.lower() == "cenoura" and quanti > 0 and quanti < 10000):
	receitas = quanti // 100
	print(receitas)
elif(ingred.lower() == "kampyo" and quanti > 0 and quanti < 10000):
	receitas = quanti // 20
	print(receitas)
elif(ingred.lower() == "nori" and quanti > 0 and quanti < 10000):
	receitas = quanti // 50
	print(receitas)
elif(ingred.lower() == "omelete" and quanti > 0 and quanti < 10000):
	receitas = quanti // 200
	print(receitas)
elif(ingred.lower() == "pepino" and quanti > 0 and quanti < 10000):
	receitas = quanti // 150
	print(receitas)	
elif(ingred.lower() == "salmao" and quanti > 0 and quanti < 10000):
	receitas = quanti // 300
	print(receitas)	
elif(ingred.lower() == "shitake" and quanti > 0 and quanti < 10000):
	receitas = quanti // 150
	print(receitas)
else:
	print("Entrada invalida")

