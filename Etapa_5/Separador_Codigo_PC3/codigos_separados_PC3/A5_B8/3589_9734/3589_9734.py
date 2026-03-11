import numpy as np
acertos.array = []
total = 0

for anel in acertos:
	if anel ==1:
		total +=80
	elif anel == 2:
		total+= 40
	elif anel == 3:
		total += 20
	elif anel == 4:
		total+= 10
		print(total)