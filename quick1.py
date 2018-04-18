def partition(a,low,high):
    i=low-1
    pivot=a[high]
    for j in range(low,high):
        if a[j]<=pivot:
            i=i+1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[high]=a[high],a[i+1]
    return i+1

def quicksort(a,low,high):
    if low<high:
        pi=partition(a,low,high)
        quicksort(a,low,pi-1)
        quicksort(a,pi+1,high)
    
    


n=int(input("enter the size of list"))
a=[]
for i in range(n):
    
    x=int(input("enter "+str(i+1)+"Number"))
    a.append(x)
print("entered list is.....",a)
quicksort(a,0,len(a)-1)
print("sorted list is ....")
for i in range(len(a)):
      print('%d'%a[i])
