from numpy import*

msg = array(eval(input("digite a mensgem numerica:")))

msg_sb = zeros(size(msg), dtype=int)

for i in range(size(msg)):
	msg_sb[i] = msg[i] * msg[i]
		
print(msg_sb)
