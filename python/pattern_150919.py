#sourcecode
n=int(input())
for i in range(n//2):
    for j in range(i+1):
        print(i+1,end='')
    for j in range(n-i):
        print(n-i,end='')
    print(end='\n')
#print the follg. pattern
    
'''
Sample IP:
6

Sample OP:
1666666
2255555
3334444
'''
