#swap two number and tell which is greater

print('1-swap two number\n2-Comparrision')
i=int(input('choice:'))
if i==1:
    a=int(input(' Enter your 1st Number'))
    b=int(input('Enter your 2nd Number'))
    if len(str(a)) !=2 or len(str(b)) !=2:
        print('Please select Proper length')
    else:
        temp=a
        a=b
        b=temp
        print('Value after swapped A is:',a)
        print('Value after swapped B is:',b)
if i==2:
    a=int(input(' Enter your 1st Number'))
    b=int(input('Enter your 2nd Number'))
    if len(str(a)) !=2 or len(str(b)) !=2:
        print('Please select Proper length')
    else:
        if a>b:
            print(a,'Is greater')
        else:
            print(b,'Is greater')
if i>2:
    exit()
    

