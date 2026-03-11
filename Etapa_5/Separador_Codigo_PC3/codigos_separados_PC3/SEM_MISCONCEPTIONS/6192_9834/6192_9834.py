casa =  input("qual casa caiu:").upper()

preta = 0

while casa!= "S":
	if casa == "PRETA":
		preta += 1

	casa = input("qual caiu?:").upper()
	
print(preta)