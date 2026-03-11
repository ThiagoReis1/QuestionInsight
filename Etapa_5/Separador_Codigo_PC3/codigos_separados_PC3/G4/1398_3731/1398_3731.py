t1= float(input("tempo em minutos: "))

ct =5000+100*t1

ct2 = 8000+100*200+90*(t1-200)
if (t1 <= 200):
	t1=ct
else :
	t1=ct2
print(round(t1,2))