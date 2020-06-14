# Python script to print sum of first N natural numbers

N = int( input ( "Enter a natural number = " ) )
x = 1
fact = 1 

while ( x <= N ) :
    fact *= x ;
    x += 1 ;

print ("The factorial of %d is = %d" %(N, fact) )




# Python script to print product of first N natural numbers

N = int( input ( "Enter a natural number = " ) )
x = 0
prod = 1 

while ( x < N ) :
    prod *= (2*x+1) ;
    x += 1 ;

print ("The product of first %d odd numberrs is = %d" %(N, prod) )

