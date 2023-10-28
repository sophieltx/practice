N,M,X,Y = map(int,input().split())
if N >= 1 and M <= 10000 and X>= 1 and Y<= 10 and Y != X:
    a = (N-M*Y)//(X-Y)
    b = M - a
    if a < 0 or b < 0:
        print ("-1 -1")
    else : print (a,b)
else : print ("-1 -1")
