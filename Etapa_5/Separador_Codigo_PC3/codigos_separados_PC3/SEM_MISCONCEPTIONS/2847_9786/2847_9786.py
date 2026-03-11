from numpy import*

senha = array(eval(input('')))
senha_new= zeros(size(senha), dtype= int)

for i in range(size(senha)):
	senha_new[i] = senha[i] **2
print(senha_new)