# This is a programme to show that variables are dynamically typed in python
x = 5 ;
print ( type ( x ) ) ;

x = 5.456 ;
print ( type ( x ) ) ;

x = " hello " ;
print ( type ( x ) ) ;

# To print value of x
x = 234 ;
print ( x ) ;

# To print Id of variable
x= 3 ;
print ( id ( x ) ) ;

# memory allocation in python is basede on reference concept
y = x ;
print ( id ( y ) ) ;

y = 2 ;
print ( id ( y ) ) ;
print ( id ( x ) ) ;