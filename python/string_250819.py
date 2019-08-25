#sourcecode
s=input()
for i in range(len(s)):
    if i%2==0:
        print(s[i],end='')
    else:
        print("*",end='')
print('\n')
for i in range(len(s)):
    if i%2:
        print(s[i],end='')
    else:
        print("*",end='')
        
# Sample IP:
# abcdefg

# Sample OP:
# a*c*e*g
# *b*d*f*
