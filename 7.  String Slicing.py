# operation on strings
names = """cry today to smile tomorrow"""
print(names[: 5])
print(names[0: 7]) #0 to 7-1
print("Will print Start to End->\n", names[: ])

print(names[7: 17])#start index to end-1 index
print(names[0: -2]) # print(names[0:len(names) -2])
print(names[-28 : -8]) # print(names[len(names) - 28:len(names) -8])

print(len(names)) #total length of a string



'''
# Quick Quiz

nm = "Harry" 
print(nm[-4: -2]) 
len(nm) = 5
->print(5-4: 5-2) -> print(1: 3) 1 to 3-1
output: ar
'''