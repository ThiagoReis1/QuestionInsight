p = int (input ("Qual a populacao inicial de tambaquis? "))
t = float (input("Qual a taxa anual de crescimento "))
n = int (input ("Quantos tambaquis sao retirados anualmente? "))
c = 1
while (p >= 0):
	p = p + p * (t) - n
	c = c + 1
print (c)	