#Your code below
x,y=map(int,input().split())
for i in range(1,max(x,y)+1):
    if( x%i is 0 and y%i is not 0):
        print(i,end=' ')
#factor of x but not y

'''
Sample IP: 
12 14 

Sample OP:
3 4 6 12
'''
