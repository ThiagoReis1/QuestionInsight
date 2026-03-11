c = float(input())

if(c>=0 and c<=10):
	valor=(c*3) + 15
	print(round(valor,2))
elif(c>10 and c<=15):
	valor=(c*3.5) + 20
	print(round(valor,2))
elif(c>15 and c<=20):
	valor=(c*4) + 25
	print(round(valor,2))
elif(c>20):
	valor=(c*4.5) + 30
	print(round(valor,2))