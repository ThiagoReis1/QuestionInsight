from numpy import*

senha = array(eval(input("digite a senha: ")))
cod = zeros(size(senha), dtype = int)

for i in range(size(senha)):
	if senha[i] == 9:
		cod[i] == 0
	else:
		cod[i] = senha[i] + 1
print(cod)