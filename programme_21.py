# Python script to set strings in dictionary order

x = input ("Enter first string = " ) 
y = input ("Enter second string = " ) 
z = input ("Enter third string = " )

if ( x > y ) :
    if ( x > z ) :
        if ( z > y ) :
            print ( y , z , x , sep = "," )
        else :
            print ( z , y , x , sep = "," )
    else :
        print ( y , x , z , sep = "," )

else :
    if ( y > z ) :
        if ( x > z ) :
            print ( z , x , y , sep = "," )
        else :
            print ( x , z , y , sep = "," )
    else :
        print ( x , y , z , sep = "," )