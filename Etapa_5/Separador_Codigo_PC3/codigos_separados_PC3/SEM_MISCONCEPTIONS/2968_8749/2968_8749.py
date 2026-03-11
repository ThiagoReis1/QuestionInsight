comida=input('L ou S:')
qq=int(input())
vd=int(input(''))

if(comida=="L"):
   calculo=qq*5+vd*4
else:
	calculo=qq*3.5+vd*4
print(round(calculo,2))
