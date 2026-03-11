populacao = int(input("população de tracajás: "))
taxa = float(input("taxa anual: "))
Roubo = int(input("quantidade de tracajás roubados: "))
t = 0
comercio = 500 
while (Roubo <= populacao):
	t = t + 1
	populacao = populacao // taxa / 100
	populacao = populacao - comercio
	populacao = populacao - Roubo
print(t)
	

	
	