#sourcecode
n=input()
a,l="aeiouAEIOU",""
for i in n:
    if i in a:
        l=l+i
l=l[len(l)-1]+l[0:]
k=0
for i in range(len(n)):
    if n[i] not in a:
        print(n[i],end='')
    else:
        print(l[k],end='')
        k+=1
#clockwise rotate cowels
#rotate by one positions

''' 
Sample IP:
aeiou

Sample OP:
eioua 
'''
