#swapping in diff ways..

a = 5
b = 10
print(" a = 5 and b= 10\n")

#First way

x = a
y = b

x ^=y
y ^= x
x ^= y

a = x
b = y

print("a = ", a , " and b = ", b , "\n")

#Second way

(a, b) = (b,a)
print("a = ", a , " and b = ", b , "\n")