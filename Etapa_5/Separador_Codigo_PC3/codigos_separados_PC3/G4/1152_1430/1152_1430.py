nb = int(input())
np = int(input())
npr = int(input())
pb = float(input())
pp = float(input())
ppr = float(input())
i = 1
while (nb + np < npr):
	nb += nb * (pb/100)
	np += np * (pp/100)
	npr += npr * (ppr/100)
	i += 1
print(i)