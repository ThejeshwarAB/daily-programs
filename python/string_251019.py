#sourcecode
s=input()
i=0
j=len(s)-1
while i<j:
    print(s[:i]+"("+s[i]+")"+s[i+1:j]+"("+s[j]+")"+s[j+1:])
    i,j=i+1,j-1
if i==j:
    print(s[:i]+"("+s[i]+")"+s[i+1:])
#print the required pattern

''' 
Sample IP:
hide

Sample OP:
(h)id(e)
h(i)(d)e
'''
