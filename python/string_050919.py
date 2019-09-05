#sourcecode
s=input()
for i in range(len(s)):
    for j in range(len(s)-i):
        print(s[len(s)-i-1],end='')
    for k in range(i+1):
        print(s[i],end='')
    print(end='\n')
#print the pattern req.

'''
Sample IP:
SKILL

Sample OP:
LLLLLS
LLLLKK
IIIIII
KKLLLL
SLLLLL
'''
