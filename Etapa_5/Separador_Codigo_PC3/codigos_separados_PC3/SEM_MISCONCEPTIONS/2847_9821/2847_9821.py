from numpy import*

senha = array (eval(input("numeros:")))
senhan = zeros(size(senha), dtype=int)

for i in range (size(senha)):
	senhan[i] = senha[i] ** 2
		
print(senhan)