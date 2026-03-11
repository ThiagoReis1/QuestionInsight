volume= float(input("volume de agua consumida"))
conta= ((0.37 * volume) + 15) 
imposto= conta * 0.35
total= conta + imposto

print(round(total, 2))
