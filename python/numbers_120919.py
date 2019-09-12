#sourcecode
l=list(map(int,input().split()))
s=int(input())
x,y=0,0
for i in range(len(l)):
    if l[i]==s:
        break
x=sum(l[:i])
y=sum(l[i+1:])
print(min(x,y))
#find x elmt. in list
#find left, right sum
#print min of the sum

'''
Sample IP:
1 2 3 4 5 6 7 8 9

Sample OP:
10
'''
