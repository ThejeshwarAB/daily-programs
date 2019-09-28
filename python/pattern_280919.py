#sourcecode
n=input()
m=abs(int(n))
p=str(m)
if(int(p[0])%2==0):
    for i in range(len(p)):
        print("*",end='')
else:
    print(n)
#print *s if first digit is even
#print original no itself if not

'''
Sample IP:
-49

Sample OP:
**
'''
