lim = float(input("lim:"))

v_1 = float(input("v1:"))
v_2 = float(input("v2:"))
v_3 = float(input("v3:"))
v_4 = float(input("v4:"))

v_total = (v_1 + v_2 + v_3 + v_4)

if (v_total <= lim):
	print(round(v_total , 2),"Dentro do limite")		
			
else:
	print(round(v_total , 2),"Estourou o limite")