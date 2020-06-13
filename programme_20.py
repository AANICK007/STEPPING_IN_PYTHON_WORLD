# Python script to find the no. of days in a month

month = int ( input ("Enter the month number = " ) )

if ( month > 0 and month <= 12 ) :
    if ( month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 ) :
        print ("The days are = 31 " )
    elif  ( month == 4 or month == 6 or month == 9 or month == 11 ) :
        print ("The days are = 30 " )
    else :
        print ("The days can be = 28 or 29 " )
        
else :
    print ("Invalid month")
    
    
    

# Python script to find nature of roots of a quadratic equation

a = int ( input ("Enter the coefficient of x^2 = " ) )
b = int ( input ("Enter the coefficient of x = " ) )
c = int ( input ("Enter the constant term = " ) )

d = (b*b) - (4*a*c) 

if ( d > 0 ) :
    print ("The roots are real and distinct")
    
elif ( d == 0 ) :
    print ("The roots are real and equal")
    
else :
    print ("The roots are complex")