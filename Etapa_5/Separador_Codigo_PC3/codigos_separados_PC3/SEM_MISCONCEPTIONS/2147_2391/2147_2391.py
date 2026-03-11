senha = input()
i = 0
var = ""
if(len(senha)!=11):
	print("INVALIDO")
else:
	while(i<len(senha)):
		if(i%2!=0):
			var = var + str(senha[i])
		i = i + 1
	print(var)