# Python script to calculate square of a number

x = int ( input ( "Enter a number = " ) ) ;

print ( "The square of",x,"is =", x*x ) ;




# Python script to calculate area of a tringle

a = int ( input ( "Enter the first side of triangle = " ) ) ;
b = int ( input ( "Enter the second of the triangle = " ) ) ;
c = int ( input ( "Enter the third of the triangle = " ) ) ;

s = ( a + b + c ) / 2 ;
print ( "The semi-perimeter of triangle =",s ) ;

from math import * ;
A = sqrt( s * ( s - a ) * ( s - b ) * ( s - c ) );
print ("The area of triangle is =", A) ;