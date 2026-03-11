from numpy import*
arra = array(eval(input("")))
v = [9 , 8, 7 , 6 ,5 , 4 , 3 , 2 , 1]

total_soma= arra[0] * v[0] + arra[1] * v[1] + arra[2]* v[2] + arra[3] * v[3] + arra[4] * v[4] + arra[5] * v[5] + arra[6] * v[6] + arra[7] * v[7] + arra[8]*v[8] 
print(total_soma%11)