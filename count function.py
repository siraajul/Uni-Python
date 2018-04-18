#('1-Uppercase and Lowercase isupper\n2-uppercase\n3-only count Vowls and consonents:')


print('1-Uppercase and Lowercase isupper\n2-uppercase\n3-only count Vowls and consonents:')
i=int(input('Choice'))
if i==1:
    a=input('A string')
    count=0
    c=0
    for i in a:
        if i.isupper():
            print('UPPERCASE IS')
            count=count+1
        else:
            print('LOWECASE IS')
            c=c+1
    print(count)
    print(c)
if i==2:
    a=input('ASTRING IS')
    upper="QWERTYUIOPASDFGHJKLZXCVBNM"
    lower="qwertyuiopasdfghjklzxcvbnm"
    for i in upper:
        print('Uppercase')
        print(i,a.count(i))
    for j in lower:
        print('LOWERCASE')
        print(j,a.count(j))
if i==3:
    a=input('A string')
    Vowels="AEIOU" or "aeiou"
    
    cons="BCDFGHJKLMNPQRSTVWXYZ" or "bcdfghjklmnpqrstvwyz"
    for i in Vowels:
        print('voWELS IS\n')
        print(i,a.upper().count(i) or a.lower().count(i))
    for j in cons:
        print('Consonents\n')
        print(j,a.upper().count(j) or a.lower().count(j))
if i>3:
    exit()
