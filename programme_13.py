# this is the use of 'import'
import math ;
x = math.factorial(5) ;
print( x ) ;

x = math.sqrt(81) ;
x = math.sqrt(81) ;
print ( x ) ;
 
# see any module in python
help(math) ;

# this is the use of 'as'
import math as m ;
x = m.factorial(12) ;
print( x ) ;
x = m.log(1) ;
print( x ) ;

# this is the use of 'from'
from math import factorial
x = factorial(6) ;
print( x ) ;

from math import sqrt ;
x = sqrt(8) ;
print( x ) ;

#if want to import 2 modules
from math import factorial , log
x = log(10) ;
print( x ) ;
x = factorial(6) ;
print( x ) ;

#if want to import all modules 
# use      ----->>>      from math import * ;
from math import * ;
x = gcd( 4 , 6 ) ;
print( x ) ;