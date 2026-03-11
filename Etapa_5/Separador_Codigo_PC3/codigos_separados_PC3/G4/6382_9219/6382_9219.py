from numpy import*

msg = array(eval(input()))
mv = zeros(size(msg), dtype=int)

for i in range(size(msg)):
	if (msg[i] == 9):
		mv[i] = 0
	else:
		mv[i] = (msg[i] + 1)**2

print(mv)