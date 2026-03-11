from numpy import*

senha = array(eval(input('')))
new = zeros(size(senha), dtype='int')

for i in range(size(senha)):
	if senha[i]== 9:
		new[i] = 0
	else:
		new[i] = senha[i] + 1
print(new)