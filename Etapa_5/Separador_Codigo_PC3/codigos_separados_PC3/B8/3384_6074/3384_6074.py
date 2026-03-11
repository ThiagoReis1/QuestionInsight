onca = input()
valor = float(input())

if(onca == "K"):
	oz = 35.274*valor
	print(round(oz,2))
elif(onca == "O"):
	oz = valor/35.274
	print(round(oz,2))