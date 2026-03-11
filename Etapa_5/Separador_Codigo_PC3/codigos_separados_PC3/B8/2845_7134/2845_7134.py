from numpy import *
msg = array(eval(input("mensagem:")))
final = zeros(size(msg), dtype = int)

for i in range(size(msg)):
	if msg[i] <= 8 and msg[i] >= 0:
		final[i] = msg[i] + 1
	elif msg[i] == 9:
		final[i] = 0
		

print(final)