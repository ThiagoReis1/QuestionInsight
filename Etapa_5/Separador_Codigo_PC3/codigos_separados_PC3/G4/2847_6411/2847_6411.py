from numpy import*

msg = array(eval(input("Digite a senha: ")))

for i in range(size(msg)):
	msg[i] = msg ** 2
print(msg)