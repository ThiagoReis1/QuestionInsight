num = int(input())

divisi = 0
if num%3 == 0:
	divisi+=3
if num%5 == 0:
	divisi+=5
	
if divisi == 5:
	print("Plact")
elif(divisi == 3):
	print("Plunct")
elif(divisi==8):
	print("Zuuum")
else:
	print(num)