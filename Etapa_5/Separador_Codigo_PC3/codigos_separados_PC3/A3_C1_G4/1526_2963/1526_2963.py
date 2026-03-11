qi = int(input("quantidade incial de mana:\n"))
qd = int(input("quantidade de mana que ela gasta por dia:\n"))
rn = int(input("quanto de energia recupera por noite:\n"))
ma = 0
dt = 0
while (qi > 0):
	qi = qi - (qd - rn)
	mt = ma + (qd - rn)
	dt = dt + 1
	if (qi <= 0):
		print(dt)
	

	