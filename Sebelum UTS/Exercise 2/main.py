import numpy as np

# Create txt file for first number and second number
with open('number.txt','w') as f:
    f.write('9502561694858652150281747994108545943651521215096841995237040384498740803993469376602031341619585763')
with open('number1.txt','w') as f:
    f.write('2116068642696162934965789080530992805391900568978958496201555855833896833372295507803936243187061092')

# Open file    
f1 = open('number.txt').read()
f2 = open('number1.txt').read()

# Add the first number and the second number with anonymous function
add = lambda x,y: int(x) + int(y)
add(f1,f2)