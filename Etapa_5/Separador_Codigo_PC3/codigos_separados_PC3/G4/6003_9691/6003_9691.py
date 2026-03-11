c= int(input("cenouras compradas: "))
t1= c*1.20
t2= c*0.90
total= t1 + t2
if total <= 5:
	print(round(t1,2))
else:
	print(round(t2,2))
