nb= int(input("numero de bacterias: "))
nh= int(input("numero de horas: "))

cont= 0
ac= nb

while cont<nh:
	n= int((ac*2)/100) 
	ac= ac+n
	cont= cont+1
print(ac)