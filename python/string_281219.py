#sourcecode
s=input()
a="aeiou"
c=0
for i in range(len(s)):
    if s[i] in a and c==0:
        print("{",end='')
        c=1
    if  s[i] not in a and c==1:
            print("}",end='')
            c=0
    print(s[i],end='')
if c==1:
    print("}")
#curly braces around vowels

'''
Sample IP:
aeiourhythm

Sample OP:
{aeiou}rhythm
'''
