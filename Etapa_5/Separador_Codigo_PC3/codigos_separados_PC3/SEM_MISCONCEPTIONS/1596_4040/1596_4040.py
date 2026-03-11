from numpy import *

# Entries

grades = array(eval(input("Insert vector containing grades: ")))

# Definitions

s = size(grades)
avarage = 0

# Processing

for s in range(s):
	avarage += grades[s]

avarage -= min(grades)
avarage = round((avarage/(s)),2)
print(avarage)