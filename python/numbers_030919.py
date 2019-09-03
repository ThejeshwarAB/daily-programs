#sourcecode
n,x=map(int,input().split())
n=bin(n)[2::]
n=n[len(n)-x:]
print(int(n,2))
#find last x bits of n in bin.
#print the req dec. equivalent

'''
Sample IP:
10 3

Sample OP:
2
1(010)
'''
