pc=float(input())

ml1= pc*(100/100)
ml2= pc*(50/100)
ml3= pc*(40/100)
ml4= pc*(30/100)



if(pc<=50):
	r=pc+ml1
	print(round(r, 2))
elif((pc>=50.01) and (pc<=100)):
	s=pc+ml2
	print(round(s, 2))
elif((pc>=100.01) and(pc<=500)):
	t=pc+ml3
	print(round(t, 2))
else:
	u=pc+ml4
	print(round(u, 2))
	