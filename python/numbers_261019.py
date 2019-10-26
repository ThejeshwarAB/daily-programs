#sourcecode
x,y=map(int,input().split())
l=[]
for i in range(1,max(x,y)+1):
    if x%i==0 and y%i!=0:
        l.append(i)
    if y%i==0 and x%i!=0:
        l.append(i)
l.sort(reverse=True)
for i in l:
    print(i,end=' ')
if l==[]:
    print("-1")
#find uncommon factors
#print it in des order

'''
Sample IP:
7 2

Sample OP:
7 2 
'''
