from math import*  
p = float(input())  
 
fkg = p * 43.21 

taxa = 25 

ficms = ((fkg + taxa) * 62) / 100

ftotal = fkg + ficms + taxa 

print (round(ftotal,2))
