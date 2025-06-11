# to convert one data type to another
a = "1"
a = 1
b = "2"
b = 2
print(a+b)#by default it will take the int value only

print(str(a) + str(b))
print(int(a) + int(b))


c, d = "Harry", "Bhai"
print(int(c) + int(d))#error
print(c+d)