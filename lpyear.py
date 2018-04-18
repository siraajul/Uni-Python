#calculate leap year or not

a=int(input('Input year'))
if len(str(a)) !=4 :
       print('ERROR')
else:
    lpyear=a%4
    if lpyear==0:
        print('This is leap year',a)
    else:
        print('not a leap year',a)
