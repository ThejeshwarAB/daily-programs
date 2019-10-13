#sourcecode
n,k=map(int,input().split())
l=list(map(str,input().split()))
x=[]
for i in l:
    if len(i)==k:
        x.append(i)
if x==[]:
    print("-1")
else:
    print(min(x))
#print min of k digit nos.
#if no k digit no.print -1

''' 
Sample IP:
4 2
111 11 222 22

Sample OP:
11
'''
