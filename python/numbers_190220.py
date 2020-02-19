#sourcecode
n=input()
l=list(map(int,input().split()))
x,y=map(int,input().split())
s=0
for i in l:
    if i in range(x,y+1):
        s+=i
print(s)
#print sum of nos in given range

'''
Sample IP:
5 
1 2 3 4 5
2 3

Sample OP:
5
'''
