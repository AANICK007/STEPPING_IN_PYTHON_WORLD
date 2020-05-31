# This is a progrramme to study type conversion in python

x = " 123 " ;
y = 5 ;

""" if do x + y
                the programme will give error
                so  we do ......................  """

z = int( x ) + y ;

print ( x , y , z ) ;

print ( type ( x ) ) ;
print ( type ( y ) ) ;
print ( type ( z ) ) ;

# to print UNICODE of variables

x = 'A' ;
y = ord ( x ) ;
print ( y ) ;