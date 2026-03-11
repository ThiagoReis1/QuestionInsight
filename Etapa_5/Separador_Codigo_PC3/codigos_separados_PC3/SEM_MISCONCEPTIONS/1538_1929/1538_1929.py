x = float(input(""))
k = int(input(""))
serie = 0
t = 0
i = 0
while (i < k):
	if (t%4 == 0):
		serie = serie + (x**t)
 	if (t%4 != 0):
		serie = serie -(x**t)
		serie = serie -(x**t)
	t = t + 2
	i = i + 1
print(round(serie, 8))
	
