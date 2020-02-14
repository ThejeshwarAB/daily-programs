#sourcecode
n,p=int(input()),[]
l=list(map(str,input().split()))
x,y=map(int,input().split())
p=[i for i in l if len(i)==x and int(i)%y==0]
if p==[]:
    print("-1")
else:
    for i in p:
        print(i,end=' ')
#print if no. in list is of len x
#print if no. in list is div by y

'''
Sample IP:
5
1 22 33 44 5
2 11

Sample OP:
22 33 44
'''
