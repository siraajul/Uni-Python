def sum():
    print('1-addition\n2-substraction\n3-multification\n4-division')
    i=int(input('choice'))
    if i==1:
        a=int(input('1st number'))
        b=int(input('2nd number'))
        c=a+b
        print(c)
    if i==2:
        a=int(input('1st number'))
        b=int(input('2nd number'))
        c=a-b
        print(c)
    if i==3:
        a=int(input('1st number'))
        b=int(input('2nd number'))
        c=a*b
        print(c)
    if i==4:
        a=int(input('1st number'))
        b=int(input('2nd number'))
        c=a/b
        print(c)
sum()
    
