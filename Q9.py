#roots of QE with all three cases

from math import sqrt

#taking coeff a ,b and c 

a,b,c= map(int,input("Enter coefficients a,b & c in ax^2 + bx +c = 0 ~~~ " ).split())

determinant = (b**2 - (4*a*c))
    

#real and equal roots
if determinant == 0:
    r = (-b)/(2*a)
    print("roots are = ", r," and ", r)

else:
    d = sqrt(abs(determinant))
    D = (d/(2*a))
    r = (-b)/(2*a)  
    

    #real and different roots 
    if determinant > 0 :
        print("roots are =" , r + D , "and ", r - D )

    #imaginary roots
    else :
        print("roots are =", r ,"+ i",D,"and ", r,"- i",D)


