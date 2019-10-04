#sourcecode
x,y=map(int,input().split(' '))
x=str(bin(x))
y=str(bin(y))
c=0
x=x[2:]
y=y[2:]
x=x[::-1]
y=y[::-1]
for i in range(len(y)):
    if x[i] is not y[i]:
        c+=1
c+=len(x)-len(y)
print(c)
#print no. of bit changes from x to y

''' 
Sample IP:
5 4

Sample OP:
1
{
5=101
4=100
}
'''
