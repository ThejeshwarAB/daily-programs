#sourcecode
n=input()
l=list(map(int,input().split()))
c={}
for i in l:
    c[i]=0
    for j in range(1,i+1):
        if int(i)%j==0:
            c[i]+=1
print(min(c.values()))
#find the no. with min. factors
#print the count of min. factors

'''
Sample IP:
3
10 12 100

Sample OP:
4
(10 has least no. of factors)
(They are 1,2,5,10 & count=4)
'''
