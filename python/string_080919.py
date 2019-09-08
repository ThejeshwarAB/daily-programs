#sourcecode
s,l=input(),""
for i in range(len(s)-1):
    if s[i].lower() not in "aeiou"and s[i+1].lower() in "aeiou":
        l=l+(s[i]+s[i+1]+" ")
print(l)
#check if vowel is followed by consonant
#if present, print them adding space b/w

'''
Sample IP:
volcano

Sample OP:
vo ca no
'''
