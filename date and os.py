#import function..

print('1-path of py\n2-time and date\n3-systrm\n4-ip address\n5-shutdown')
print('6-remove file\n7-dict')
i=int(input('Choice'))
if i==1:
    import os
    print(os.path)
if i==2:
    from datetime import date
    now = date.today()
    print(now)
if i==3:
    import sys
    print(sys.api_version)
    print(sys.getsizeof)
    print(sys.modules)
if i==4:
    import os
    while True:
        check = input("Want to shutdown your computer ? (y/n): ")
        if check == 'n':
            break
	else:
            os.system("shutdown /s /t 1")
