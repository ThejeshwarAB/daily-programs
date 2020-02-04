#sourcefile
l=list(map(int,input().split()))
n=int(input())
if l[0]==n or l[-1]==n:
    print("YES")
else:
    print("NO")
#print yes if begins or end with same number

'''
Sample IP:
10 20 30 40 50
50

Sample OP:
YES
'''
