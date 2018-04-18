#sum of n length number and check palendrom and reverse number

a=int(input('input you choice should be greater than 3'))
su=0
rev=0
pa=0
temp=a
if len(str(a)) !=3 :
    print('wrong choice')
else:
    while a>0:
        rem=a%10
        su=su+rem
        pa=pa+rem*rem*rem
        a=a//10
        rev=rev*10+rem
temp=pa
print('sum of cubenumber is',pa)
print('========================================\n')

if pa==temp:
    print(pa,'number is armstong')
else:
    print('Number is not armstrong\n')
print('=========================================')
        
print('Sum of given number is',su)

print('==========================================')
            
print('Reverse of Given NUMBER is:',rev)
print(pa)
    
