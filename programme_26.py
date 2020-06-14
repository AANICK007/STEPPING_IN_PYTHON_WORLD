# Python script to print sum of first N natural numbers

N = int( input ( "Enter a natural number = " ) )
x = 1
suum = 0 

while ( x <= N ) :
    suum += x ;
    x += 1 ;

print ("The sum of first %d natural numbers is = %d" %(N, suum) )





# Python script to print sum of first N odd numbers

N = int( input ( "Enter a natural number = " ) )
x = 0
suum = 0 

while ( x < N ) :
    suum += (2*x + 1) ;
    x += 1 ;

print ("The sum of first %d odd numbers is = %d" %(N, suum) )