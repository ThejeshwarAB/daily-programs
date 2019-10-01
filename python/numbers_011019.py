#sourcecode
def digs(n):
    s=0
    while(n):
       s=s+n%10
       n=n//10
    return s
#func to calc digital sum

n=input()
l=[]
for i in n:
    l.append(int(i))
for i in range(len(n)-1):
    t=l[i]+l[i+1]
    if t>=10:
        t=digs(t)
    print(t,end='')
#print req dig sum of the number

'''
Sample IP:
123

Sample OP:
35
{
1+2=3
2+3=5
}
'''
