#sourcecode
n=input()
t=[]
l=list(map(int,input().split()))
for i in range(len(l)-1):
    t.append(abs(l[i]-l[i+1]))
print(max(t))
#print max abs difference

'''
Sample IP:
5
1 2 3 4 7

Sample OP:
4
'''
