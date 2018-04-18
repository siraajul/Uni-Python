#odd ,even and prime positve, negative

print('1-odd and even\n2-prime\n3-positive and negative')
i=int(input('choice'))
if i==1:
    a=int(input('a number'))
    if a%2==0:
        print('even number')
    else:
        print('odd number')
if i==2:
    a=int(input('a number'))
    for j in range(1,a):
        if a%j!=0:
            print('prime number',a)
        else:
            print('not a prime number')
if i==3:
    a=int(input('a number'))
    if a>0:
        print(a, 'is Positive number')
    else:
        print(a,'Negative Number')
    
