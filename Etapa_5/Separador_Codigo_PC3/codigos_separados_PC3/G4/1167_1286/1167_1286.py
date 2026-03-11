n = int(input())

s = -1/8
i = 1
num = 2
j = 1

while(i < n):	
 j +=2	
 if(i%2 ==0):
  s -= (num**2)/(7+j)	
 else:
  s += (num**2)/(7+j) 		
 num+=1 
 i+=1
print(round(s,11))