# This is s programmr to study relational operators in python

x = 3>2 ;
print ( x ) ;

x = True ;
y = int( x ) ;
print ( y ) ;

x = bool(0) ;
print ( x ) ;
x = bool(5) ;
print ( x ) ;

x = "ABC" == "DEF" ;
print ( x ) ;
x = "ABC" < "DEF" ;
print ( x ) ;
x = "AB" == "AB" ;
print ( x ) ;

x = 2+3j == 3+4j ;    # this is comparision of complex numbers
print ( x ) ;
x = 3+4j == 3+4j ;
print ( x ) ;

x = 5 > 4 > 3 ;     # this is operators chaining
print ( x ) ;
x = 5 > 4 > 3 < 2 ;
print ( x ) ;

x = True == 1 ;
print ( x ) ;
x = False == 0 ;
print ( x ) ;
x = True == 4 ;
print ( x ) ;
x = True < 5 ;
print ( x ) ;