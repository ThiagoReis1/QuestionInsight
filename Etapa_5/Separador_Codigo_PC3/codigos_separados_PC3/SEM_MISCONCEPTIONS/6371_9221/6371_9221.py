from numpy import*

mensagem= array(eval(input("digite: ")))
mensagemsub= zeros(size(mensagem), dtype= int)

for i in range(size(mensagem)):
	if (mensagem == 0):
		mensagemsub[i] = 9 ** 2
	elif (mensagem
		mensagemsub[i] = mensagem +1
		
		#ensagemsub[i]= mensagem[i] * mensagem[i]
print(mensagemsub)