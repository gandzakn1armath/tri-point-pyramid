import math
while True:
        a = int(input("Enter the tri-point side"))
        h = math.sqrt(a**2 - (a/2)**2)
        r = a*h / 2
        b = int(input("enter the side of the pyramid"))
        x = b**2 - (a/2)**2
        y = 4*(a*x/2)
        S = r + y
        print ("the surface of the pyramid"+str(S))
