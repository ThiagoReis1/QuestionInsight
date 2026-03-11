valorMens = float(input())
numChild = int(input())

if(numChild == 1):
	valorF = numChild * valorMens * 9/10
elif(numChild == 2):
	valorF = numChild * valorMens * 7/10
else:
	valorF = numChild * valorMens * 6/10
	
print(round(valorF,2))