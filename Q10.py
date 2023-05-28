#showcasing uses of arithmetic,logical,bitwise,relational,assignment and membership operators

a = 1
b = 2

'''arithmetic operators'''

#addition
print("Arithmetic Operators:")
print(a,"+", b ,"=", a+b)

#subtraction
print(a ,"-",b,"=",a-b)

#division
print(a,"/",b,"=",a/b) 

#multiplication
print(a,"X",b,"=",a*b)

#modulo
print(a,"%",b , "=",a%b)

#floor division
print(a,"//",b,"=",a//b)

#power
print(a,"^",b,"=",a**b)

'''Logical operators'''
print("Logical Operators:")

print("let a = True(>0) and b = False(0)")
a=True
b=False

#AND
print("a AND b = ",a and b )

#OR
print("a OR b = ", a or b)

#NOT 
print("NOT a =",not a )


'''Bitwise Operators''' 

print("Bitwise Operators:")

""" def decToBin(num):
    if num >= 1:
        decToBin(num//2)
    else:
        x= num%2
        return x    
a=2
b=3
x = decToBin(a)

y = (b)

print("\n" , y)"""
#SHFT+ALT+A

a=1001
b=10101

#bitwise AND or logical conjunction(a&b = a X b)
print(a ,"&",b,"=",a&b)

#bitwise Or logical disjunction(a|b = a+b -(aXb))union
print(a ,"|",b,"=",a|b)

#bitwise XOR ab' + a'b (no logical counterpart but can be shown as a func)
#exclusive disjunction (always opposite bits produce a 1)
#(a ^ b = (a+b)mod2)
print(a ,"^",b,"=",a^b)

#bitwise NOT ~a = 1 - a 
print("~",a,"=",~a & 15) # bitmask as python has no unsigned int support

'''BITWISE shift operators'''

print("Bitwise Shift Operators:")
a=101
b=2
#Bitwise left shift a << n = a X 2^n
print(a ,"<<",b,"=",a<<b and 4 ) #for bitmasking so only three values remain 

#Bitwise right shift a >> n = floor(a/2^n)
print("5 >> 1  = ",5>>1,"like 5//2")
print("5 >> 2 =",5>>2,"like 5//4")

#for simulating logical right shift in python
from ctypes import c_uint32 as unsigned_int32
print("simulating logical right shift = -100 >> 1=",unsigned_int32(-100).value >> 1) # related to max bits for int in java

#a func for lrshift
def lrs(signed_int,places,num_bits= 32):
    unsigned_int = signed_int % (1 % num_bits) 
    return unsigned_int >> places

print("func on lrs= ",lrs(-100,1))


'''An arithmetic right shift (>>), sometimes called the 
   signed right shift operator, maintains the sign of a number by 
   replicating its sign bit before moving bits to the right'''

'''Relational Operators'''

print("Relational Operators:")

#greaater than
print("5 > 4 = ", 5 > 4)

# less than
print("5 < 4 = ", 5<4)

# greater than or equal to
print('5 >= 10 =', 5 >= 10)

# less than or equal to
print("5 <= 10 =",5 <= 10)

# equal to
print("5 == 10 = ", 5 == 10)

# not equal to
print("5 != 10 =", 5 != 10)

'''Assignment Operators'''

print("Assignment Operators:")

# assign 
a = 5 + 2
print("a = 5 + 2",a)

#add and assign
b += a
print("b += a",b)

#subtract and assign
b -= a
print("b -= a",b)

#multiply AND
a *= b
print("a *= b",a)

# divide AND
a= 10
b= 5
a /= b
print('a /= b =',a)

# modulus AND
b %= a
print('b %= a',b)

# floor AND
a= 10
b = 15
b //= a
print('a %= b =',b)

# exponent AND
b **= a
print('b %= a =',b)

# bitwise AND
a = 100
b = 11
b &= a
print('b &= a',b)

# bitwise OR
b |= a
print('b |= a',b)

# bitwise xOR 
a ^= b
print('a ^= b',a)

# bitwise right shift
a =100
b=2
print('a = ', a,"b = ", b)
a >>= b
print("a >>= b", a)

# bitwise left shift
a <<= b
print("a <<= b", a)


'''Membership Operators'''

print("Membership Operators:")

# in operator
print("g in GFG =  ", 'g' in 'GFG') 

dic1 = {1:"gfg" , 2:34}
print("34 in dic1 = ",34 in dic1)
print("2 in dic1 = ",2 in dic1)

# not in operator
print("34 not in dic1 = ", 34 not in dic1)


'''Identity Operators'''

print("Identity Operators:")

# compare datatypes(memory space )

# is operator
print("3 is 4 = ", 3 is 4)

x = ("hi",34)
y = ("hi",34)
print("x = ", x,"y = ", y)

z= x
print("z=x")

print("x is not z = ", x is not z)
print("x is not y = ", x is not y)
print("x != y  ", x != y)
