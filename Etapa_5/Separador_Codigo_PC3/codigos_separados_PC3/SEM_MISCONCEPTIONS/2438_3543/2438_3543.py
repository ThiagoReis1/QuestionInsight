freq=float(input("frequencia em hz"))
temp=float(input("tempo em min"))
temp_s= 60*temp
total=freq*temp_s
print(round(total))