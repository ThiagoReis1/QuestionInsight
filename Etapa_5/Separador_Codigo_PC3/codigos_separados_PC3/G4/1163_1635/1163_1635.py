lambari = int(input("informe a populaçao incial de lambaris no tanque: "))
tucunare = int(input("informe população inicial de tucunarés no tanque:  "))
tl = float(input("informe taxa mensal de crescimento do número de lambaris: "))
tt = float(input("informe taxa mensal de crescimento do número de tucunarés : "))

l = lambari
t = tucunare
i = 0
while(l > t):
	l = l + (l * tl/100) - (2 * t)
	t = t + (t * tt/100)
	i = i + 1
print(i)
