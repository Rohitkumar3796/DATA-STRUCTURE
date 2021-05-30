import random
def binary_search(list1,val):
    l=list1[0]
    r=list1[-1]
    while l<=r:
        m=(l+r)/2
        mid=int(m)
        if list1[mid]==val:
            return mid
        elif list1[mid]<val:
            l=mid+1
        else:
            r=mid-1
    print(val)

list1=[i for i in range(1,20)]
random_choice=random.choice(list1)
print("Element Present at Index",binary_search(list1,random_choice))
print("The random choice is:",random_choice)
