print("*********************************************")

print("****ENTER FIVE SUBJECT MARK CAREFULLY INT,DBMS,CSE,PHY,MATH")

print("**********************************************")
m=int(input('enter math mark'))
p= int(input('enter physics mark'))
I=int(input('Enter internet programming mark'))
d=int(input('Enter dbms subject mark'))
c=int(input('Enter cse mark'))

print("***********************************************")

avg=(m+p+I+c+d)/5
print("************************************************")

print("percentage in math")
per=(m/100)*100
print(per)
print("************************************************")
print("percentage in physics")

per1=(p/100)*100

print(per1)
print("************************************************")
print("percentage in INTERNET PROGRANMMING")

per2= (I/100)*100
print("************************************************")
print("percentage in dbms")

per3= (d/200)*100

print(per3)

print("************************************************")
print("percentage in cse")

per4=(c/200)*100
print(per4)

print("************************************************")
print(avg)

if(avg<90 and avg>85):

    print(" your grade is A+")

if(avg> 85 and avg<80):

    print(" YOUR GRAGE IS A")

if(avg<80 and avg>70):

    print("Your grade is B+")

if(avg<70 and avg>65):
          print("yoyr grade is B")

if(avg<65 and avg>60):
          print("your garde is C")

if(avg<60 and avg>50):
          print("your grade is D")

if(avg<50 and avg>40):
          print("your grade is E")


print("************************************************")
print("************************************************")

print("***************percentage of your hole mark...********")
avgper=((m+p+I+c+d)/800)*100

print("************************************************")
print("************************************************")
print("************YOUR CGPA IS ************************")

cgpa=(avgper/9)

print("===============",cgpa,"====================")

print("************************************************")
print("************************************************")
