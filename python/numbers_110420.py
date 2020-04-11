#sourcecode
n=input()
l=list(map(int,input().split()))
x,s=[],""
for i in range(len(l)-2):
    for j in range(1,len(l)-1):
        for k in range(2,len(l)):   
            if l[i]<l[j]<l[k] and i<j<k:
                s+=str(l[i])+str(l[j])+str(l[k])
                x.append(s)
                s=""
print(len(x))
#print triplets in list order
#triplets are values in ascd.

'''
Sample IP:
5
3 1 4 7 8

Sample OP:
2

(3<4<7)
(3<4<8)
'''
