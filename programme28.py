# Python script to check if a number is prime or not

n = int( input("Enter a number : ") )

if ( n < 2 ) :
    print("This is a non prime number")

else :
    for i in range( 2 , n ) :
        if ( n % i == 0 ) :
            print("This is a non prime number")
            break
    else:
        print("The number is a prime number")




N = int( input("Enter a number : ") )

if ( N < 2 ) :
    print("Next prime number is 2 ")

else :
    while True :
        N += 1

        for i in range( 2 , N ) :
            if ( N % i == 0 ) :
                break

        else :
            print("The next prime number is ", N)
            break

