try:
    T,G,W,E,B= map(int,input().split())
    if isinstance(T,int) and isinstance(G,int) and isinstance(W,int) and isinstance(E,int) and isinstance(B,int) and G+W+E+B <= T:
        print (G+W+E+B)
    else :
        print ("-1")
except:
    print("-1")


# *X + b*Y == N and a+b == M
# N,M,X,Y = map(int,input().split())
# a = (N-M*Y)//(X-Y)
# b = M - a
# if a < 0:
#     print (a,b)
# else :
#     print ("-1 -1")
