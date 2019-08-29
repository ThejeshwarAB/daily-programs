#sourcecode
o,n,l=0,input(),list(map(int,input().split()))
for i in l:
    if i%2:
        o+=1
if o>(int(n)//2):
    print("odd")
elif o<(int(n)//2):
    print("even")
else:
    print("-1")
#print odd/even/-1 based on frequency
    
'''
Sample IP:
5
1 2 3 4 5

Sample OP:
odd
'''
