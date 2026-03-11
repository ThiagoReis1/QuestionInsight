from numpy import*
msg = array(eval(input("Qual a mensagem: ")))


for i in range(size(msg)):
	if msg[i] == 0:
		msg[i] = 9
	else:
		msg[i] = msg[i] - 1
print(msg)
