nome = input("Qual a nome da armadura: ")
dest = int(input("Qual o valor do DADO: "))

resist1 = (15 * dest) - 1
resist2 = (20 * dest) - 18
	
if (nome == "malha"):
    print(resist1)
else:	 
	 print(resist2)

