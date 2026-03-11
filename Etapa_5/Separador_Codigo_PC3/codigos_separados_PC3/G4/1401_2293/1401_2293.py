A = input("Qual o tipo de ataque?: ") 
Q  = int(input("quantidade de baforada : "))
if (A.lower() != 'maritimo'):
	print("Drogon")
	print(Q * 150)	
else:
	print("Viserion")
	print(Q * 40)