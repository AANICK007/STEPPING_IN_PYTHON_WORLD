# This is a programme to see number system handlind in python

# By default number system in python is decimal
x = 45 ;
print ( x ) ;

# to make number sytem in binary
x = 0b01100010101 ;
print ( x ) ;

# to make octal
x = 0O132467
print ( x ) ;

# to make number system in hexadecimal
x = 0X3AFB2 ;
print ( x ) ;

# to convert decinal into another systems

x = 23416 ;
print ( bin ( x ) ) ;   # to print in binary
print ( oct ( x ) ) ;   # to print in octal
print ( hex ( x ) ) ;   # to print in hexadecimal


# to  slice and get only particular number in  number system
# we slice the number from front by 2

x = 905 ;
y = bin ( x ) ;
print ( y [ 2:: ] ) ;  # cut the first two letters that denotes the number system
