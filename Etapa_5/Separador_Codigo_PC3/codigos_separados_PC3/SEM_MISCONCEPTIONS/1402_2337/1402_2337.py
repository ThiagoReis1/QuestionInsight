nome=input("digite o nome da arma")
sucesso=int(input("digite o fatot de sucesso"))

if(nome == 'machado'):
	print(30*sucesso/10)
if(nome == 'lanca'):
	print(int(5+20*sucesso/10))
	