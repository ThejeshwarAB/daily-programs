#sourcecode
n=int(input())
x=[]
for i in range(n):
    x.append(input().split(' '))
t=input()
for i in x:
    c,k=0,0
    for j in i:
        if(j[0].lower()==t[k].lower()):
            c+=1
            k+=1
        else: break
    if(c==len(t)):
        print(*i)
        break
#input n no. of strings
#print the abbreviation

'''
Sample IP:
2
world wide web
world health org
WHO

Sample OP:
world health org
'''
