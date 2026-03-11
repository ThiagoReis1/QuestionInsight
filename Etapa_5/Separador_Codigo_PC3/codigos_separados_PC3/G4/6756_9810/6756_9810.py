dr=int(input())
if(dr<15):
	tt= (175*dr)+20
elif(dr==15):
	tt= (175*dr)+16
else:
	tt= (175*dr)+10
print(round(tt,2))
