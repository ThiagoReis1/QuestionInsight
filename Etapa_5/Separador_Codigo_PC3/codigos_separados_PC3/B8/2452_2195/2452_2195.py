peso =float(input())
altura = float(input())

f = peso/altura **2
if(f < 18,5):
	print("abaixo do peso")
elif((f <= 18,5)  and (f < 25)):
	  print("normal")
elif((f <= 25) and (f < 30)):
	print("acima do peso")
elif(f >= 30 ):
	print("obeso")
