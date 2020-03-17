#sourcecode
n=int(input())
a=[]
x=list(map(int,input().split()))
s=''
p=len(str(max(x)))
for i in range(1,p+1):
    for j in range(len(x)):
        a.append(x[j]%10)
        x[j]//=10
    s+=str(max(a))
    a=[]
print(s[::-1])
#find the max at respective unit, tenth, hundth 
#form a new number by using the obtained values

'''
Sample IP:
4
123 123 211 789

Sample OP:
7289
'''
