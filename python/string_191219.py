#sourcecode
n=input()
z=len(n) 
x=0
y=z//4
for i in range(4):
    s=n[x:y]
    print(s[::-1],end=' ')
    x+=y
    y+=y
#reverse every 4 parts
#print sequence as ops

'''
Sample IP:
FfAaCcTt

Sample OP:
fF aA cC tT
'''
