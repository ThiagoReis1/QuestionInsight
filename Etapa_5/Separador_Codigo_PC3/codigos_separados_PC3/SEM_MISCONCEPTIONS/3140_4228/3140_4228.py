from numpy import*

n = array(eval(input("Numeros reais e positivos: ")))
j = 0

for i in range(size(n)):
	if (j > 0):
		j = j + 1
		
media = ((sum(n**5))/size(n))**(1/5)
print(round(media, 2))