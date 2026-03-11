quantidade_combustivel = int(input("dgite a quantidade:"))
if(quantidade_combustivel < 17.5):
	mistura = quantidade_combustivel + 10.5
elif(quantidade_combustivel >= 17.5 and quantidade_combustivel<= 35.0):
	mistura = quantidade_combustivel + 14.0
elif(quantidade_combustivel >= 35.0 and quantidade_combustivel<=50.0 ):
	mistura = quantidade_combustivel + 18.6
else:
	mistura = quantidade_combustivel + 24.5
print(round(mistura, 2))