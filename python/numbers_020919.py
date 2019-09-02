#soucecode
n=int(input())
l=list(map(int,input().split()))
s=""
t=0
for i in l:
    if(i==2):
        s+="1"
    elif(i==1):
        s+="0"
    else:
        s+=(bin(i)[::-1][1])
print(int(s,2))

#find 2nd digit in bin. of each
#form a no. with all 2nd digits
#print the no. in dec. format

'''
Sample IP:
3
10 7 1

Sample OP:
6

10: 10(1)0
07: 1(1)1
01: 0(0)1
and hence,
110:6
'''
