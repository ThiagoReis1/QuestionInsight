#luna e a maior ate alguem passar ela entao enquanto a luna for maior repita a altura mais a 
#taxa tanto da pessoa aleatoria tanto dela
alta = 1.65
taxaa = 0.02
cont = 0
alt = float(input("altura: "))
taxa = float(input("taxa: "))
while alta > alt:
	alt = alt + taxa
	cont = cont + 1
	alta = alta + taxaa
	if alta <= alt:
		print(cont)
