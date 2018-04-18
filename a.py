capacity=50
capacityremaining=capacity
n=int(input('No of itrms'))
items=[]
weight=[]
price=[]
ratio=[]
'''test
item=[computer,pendrive,clock,]
weight-[10,5,9,5,1,7,7,55,]
price=[10,55,122,77,88,55,44]
capacity=

'''
for i in range(n):
    items.append(input("enter item name"))
    weight.append(float(input("enter weight")))
    price.append(float(input("enter price")))
choice=int(input("1-minimum weight\n2-maximun ratio\n3-"))
count=0
weightofbag=0 
totalsum=0
while count<n:
    if choice==1:
        mweight=min(weight)
        pos=weight.index(mweight)
    elif choice==2:
        mprice=max(price)
        price=price.index(mprice)
        mweight=weight[pos]
    if(mweight<=capacityremaining):
        print(items[pos],"inserted into bag")
        totalsum=totalsum+price[pos]
        weightofbag=weightofbag+mweight
        capacityremaining=capacity-weightofbag
    del items[pos]
    del weight[pos]
    del price[pos]
    del ratio[pos]
    count=count+1
    if capacity==weightofbag:
        break
    print("total price in bag:",totalsum,"\n total weight of bag:",weightofbag)
