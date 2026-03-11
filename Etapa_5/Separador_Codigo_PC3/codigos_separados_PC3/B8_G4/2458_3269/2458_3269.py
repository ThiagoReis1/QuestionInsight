psd = float(input("Informe o preco sem desconto:"))
cre = int(input("Informe o codigo da regiao:"))
vt = (psd - psd * 40//100)

if(cre == 1):
	print(psd * 10//100 + vt)
elif(cre == 2):
	print(psd * 8//100 + vt)
elif(cre == 3):
	print(vt)
elif(cre == 4):
	print(psd * 2//100 + vt)
	

	