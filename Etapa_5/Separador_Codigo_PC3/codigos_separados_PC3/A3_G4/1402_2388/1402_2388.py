a= input("arma: ")
ft= int(input("fator de sucesso :"))

if  ( a == "machado"):
	d= int(30 * ft / 10)
if  (a == "lanca"):
	d= int(5 + 20 * ft / 10)

print(d)