from numpy import*
msg = array(eval(input("")))
cont = zeros(size(msg),dtype=int)
for i in range(size(msg)):
	if(msg[i]==9):
		cont[i] = 0
	else:
		cont[i] = msg[i] + 1
print(cont)