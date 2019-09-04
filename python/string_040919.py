#sourcecode
n=input()
x=n[len(n)-2]
for i in n:
    for j in range(int(x)):
        print(i,end='')
#find 10th digit as no. x
#print each digit x times

'''
Sample IP:
346

Sample OP:
333344446666
(4 is the 10th digit)
'''
