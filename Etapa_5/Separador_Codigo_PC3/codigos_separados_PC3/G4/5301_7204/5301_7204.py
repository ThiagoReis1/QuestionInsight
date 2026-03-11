v = float(input("velocidade: "))

d = v
i = 0

while d >= 40 :
	d = d - 0.02*d
	i = i + 1 

print(i)