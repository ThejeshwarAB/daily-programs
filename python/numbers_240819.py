#sourcecode
n,x=map(int,input().split())
while(x):
    y=x*n
    print(f"{x} * {n} = {y}")
    x-=1
'''
Sample IP:
4 5

Sample OP:
5 * 4 = 20
4 * 4 = 16
3 * 4 = 12
2 * 4 = 8
1 * 4 = 4
'''
