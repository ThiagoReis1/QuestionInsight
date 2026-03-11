from numpy import *

aneis = array(eval(input("Quais foram os acertos? ")))

i = 0
pont = 0 

while(i < size(aneis)):
	if(aneis[i] == 1):
		pont = pont + 100
	elif(aneis[i] == 2):
		pont = pont + 60
	elif(aneis[i] == 3):
		pont = pont + 20
	elif(aneis[i] == 4):
		pont = pont
	i = i + 1
print(int(pont))