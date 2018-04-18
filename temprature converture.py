print('WELCOME TO CALCULATER TO CALCULATER OF FARENHITE TO CELCIOUS')
print("============================================================")
print('1-Convert forenhite to celcious...\n2-Convert celcious to forenhite')
choice=int(input('Choice'))
if choice==1:
    f=int(input('INput Select Temprature of farenhite'))
    c=((f-32)*5)/9
    print("temprature in Celcious\n",c)
elif choice==2:
    c=int(input('INput Select Temprature of celcious.'))
    f=(9/5)*c +32
    print("temprature in Farenhite\n",f)
else:
    print("wrong choice")
    exit()
