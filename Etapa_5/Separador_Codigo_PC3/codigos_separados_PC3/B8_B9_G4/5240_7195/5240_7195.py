con=int(input("qual seu consumo de energia:"))

if con <100:
	f=con*0.50+50
	print(round(f,2))
elif con>=100 and con<250:
	f=con*0.75+50
	print(round(f,2))
elif con>=250 and con<500:
	f=con*1+50
	print(round(f,2))
elif con>=500:
	f=con*1.25+50
	print(round(f,2))