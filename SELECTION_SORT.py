# SELECTION SORT
n=[8,5,4,11,1]
for i in range(0,len(n)):
    min=i
    for j in range(i+1,len(n)):
        if n[min]>n[j]: #i can alos use > sign here to print descending order
            min=j
    n[i],n[min]=n[min],n[i]
print("sorted array")
# print(n)
for i in range(len(n)):
    print(n[i])
