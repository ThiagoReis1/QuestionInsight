x = float(input("digite o valor da entrada: "))
y = int(input("digite o dia da semana: "))
t = input("e dia de musica ao vivo? ")
if (y == 2 or 3 or 5 and t == "s"):
	p = x - (x * 25/100) + 20
elif (y == 1 or 4 or 6 or 7 and t == "n"):
	p = x
if (y == 2 or 3 or 5 and t == "n"):
    p = x - (x * 25/100)
elif (y == 1 or 4 or 6 or 7 and t == "s"):
    p = x + 20
print ("entrada" , x , y , t)
print (round(p ,2)