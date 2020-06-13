# Python script of pass / fail detector

v = int ( input ("Enter marks of first subject out of 100 = " ) )
w = int ( input ("Enter marks of second subject out of 100 = " ) )
x = int ( input ("Enter marks of third subject out of 100 = " ) )
y = int ( input ("Enter marks of fourth subject out of 100 = " ) )
z = int ( input ("Enter marks of fifth subject out of 100 = " ) )

avg = (v + w + x + y + z) / 5 ;

if ( avg >= 40 ) :
    print("You are PASS" )
else :
    print("You are FAIL" )