#sourcecode
n=input()
l=[]
for i in n:
    l.append(i)
x,y=0,0
o,e=0,0
for i in range(len(l)):
    if int(l[i])%2==0 and e==0:
        x=i
        e=1
    elif int(l[i])%2==1 and o==0:
        y=i
        o=1
t=l[x]
l[x]=l[y]
l[y]=t
s=""
for i in l:
    s=s+i
print(int(s))
#swap 1st odd and 1st even in no.
#print the req. swapped no. as op

'''
Sample IP:
12345

Sample OP:
21345
'''
