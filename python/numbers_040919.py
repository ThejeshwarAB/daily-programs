#sourcecode
a,b=map(int,input().split())
x,y,z=map(int,input().split())
for i in range(a,b+1):
    if i%x==0 or i%y==0 or i%z==0:
        print(i,end=' ')
#a and b are the extreme limits
#print multiples of x,y,z there

'''
Sample IP:
2 15
3 11 13

Sample OP:
3 6 9 11 12 13 15
'''
