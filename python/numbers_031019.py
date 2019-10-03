l=list(map(int,input().split()))
l.sort()
if l[0]+l[3] == l[1]+l[2]:
    print("YES")
else:
    print("NO")
#split ip 4 nos into 2 halves
#check if they have equal sum
#prints YES or NO accordingly

'''
Sample IP:
1 7 2 6

Sample OP:
YES
{
1+7=8
2+6=8
}
'''
