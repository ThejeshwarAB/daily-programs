#sourcecode
n=input()
a="aeiouAEIOU"
c,x,y=0,0,0
for i in n:
    y+=1
    if i in a:
        if c==0 and x==1 and y is not len(n):
            print('-',end='')
            c+=1
    else:
        print(i,end='')
        c=0
        x=1
#print hyphen only in middle not before or after
#print hyphen one time only between the consonants

'''
Sample IP:
Forests

Sample OP:
F-r-sts
'''
