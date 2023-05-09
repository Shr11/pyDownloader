# exchanging two no.s without a temporary variable

a , b = map(int, input("Enter a and b\n").split())

a=a+b
b=a-b
a=a-b

print("a = ", a,"and b = ",b)