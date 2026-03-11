# numeros usados; 0 a 9 se existir o numero 7 == 14

from numpy import*
msg = array(eval(input("Digite a senha: ")))
count = zeros(len(msg), dtype = int)

for i in range(len(msg)):
	if msg[i] >= 0 or msg[i] <= 9:
		count = msg * 2
print(count)
		
	