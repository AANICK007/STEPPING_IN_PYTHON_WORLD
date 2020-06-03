# This is a programme to study logical operators in python

x = 4 > 3 and 2 > 1 ;
print ( x ) ;
x = 4 > 5 and 5 > 1 ;
print ( x ) ;
x = 4 > 3 and 3 < 2  ;
print ( x ) ;

x = 3 > 4 or 3 > 2 ;
print ( x ) ;
x = 3 > 4 or 4 > 5 ;
print ( x ) ;

x = 5 and 4 ;    # if operands are non boolean result is non boolean
print ( x  ) ;   #  if first operand false result first value and if first value true the value second operand

x = 4 or 3 ;
print ( x ) ;  # this is vise versa of and operator

x = not 5 ;
print ( x ) ;
x = not ( 4 > 5 ) ;
print ( x ) ;