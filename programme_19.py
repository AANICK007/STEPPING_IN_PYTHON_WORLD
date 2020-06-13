# Python script to find greatest among three numbers

x = int ( input ("Enter first number = " ) )
y = int ( input ("Enter second number = " ) )
z = int ( input ("Enter third number = " ) )

if ( x > y ) :
    if ( x > z ) :
        print ("%d is the largest number "%x )
    else :
        print ("%d is the largest number "%z )
else :
    if ( y > z ) :
        print ("%d is the largest number "%y )
    else :
        print ("%d is the largest number "%z )
        
        
        
# Python script to find if a given year is leap or not

year = int ( input ("Enter an year = " ) )

if ( year % 4 ) :
    print ("%d is not a leap year"%year )
else :
    print ("%d is a leap year"%year )