# This is a programme to study identity operators in  python
# Identity operators are used to compare that are two variables pointing to a same memory location or not

x = 5 ;
y = 5 ;

print ( id ( x ) ) ;
print ( id ( y ) ) ;

print ( x is y ) ;
print ( x is not y ) ;

y = 6 ;

print ( id ( x ) ) ;
print ( id ( y ) ) ;

print ( x is y ) ;
print ( x is not y ) ;

# difference between (==) and (is) operators

x = 5 ;
y = 5.0 ;

print ( id ( x ) ) ;
print ( id ( y ) ) ;

print ( x is y ) ;
print ( x == y ) ;