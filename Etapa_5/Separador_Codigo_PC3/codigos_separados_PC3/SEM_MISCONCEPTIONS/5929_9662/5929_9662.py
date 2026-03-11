volume = float(input("Volume de agua:"))
total = (0.37*volume)+15
total_icms = (35/100)*total
conta_total = total+total_icms
print(round(conta_total, 2))