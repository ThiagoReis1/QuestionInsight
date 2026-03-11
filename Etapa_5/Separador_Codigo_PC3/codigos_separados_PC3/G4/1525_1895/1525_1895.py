vi = int(input("digite o v inicial"))
vb = int(input("digite o v bombeado"))
vr = int(input("digite o v retirado"))

t = 0
total = vi
while( total > 1000):
	vi = vi + vb - vr
	total = vi
	t = t + 1
	
print("",t)