#sourcecode
s=input()
a,b,c,d="aeiou","AEIOU","",""
for i in s:
    if i in a:
        c=c+i 
    elif i in b:
        d=d+i 
if (len(c)==0 and len(d)>0) or (len(c)>0 and len(d)==0):
    print("YES")
else:
    print("NO")
#print YES if vowels in same case
#if not print NO

'''
Sample IP:
aeiou

Sample OP
YES
'''
