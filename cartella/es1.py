from random import randint
def Bubble_sort(a):
    print(a)
    c=0
    swapped = True
    while swapped:
        print(c)
        c+=1
        swapped = False
        i = 1
        while i < len(a):
            
            if a[i-1]<a[i]:
                tmp=a[i-1]
                a[i-1]=a[i]
                a[i]=tmp
                swapped=True
            i=i+1
    print(a)           
    return a

list = Bubble_sort([random.randinit() for i in range(35)])
print(list)