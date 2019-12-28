#sourcecode
n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    c=0
    x=i
    while(i):
        r=i%10 
        if r%2:
            c+=1 
        i=i//10
    if c>=2:
        s+=x
print(s)
#find sum of nos with more than 2 odd digits
#print the calculated value of sum as output

'''
Sample IP:
123 222

Sample OP:
123
'''
