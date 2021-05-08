def insertion_sort(arr):
    for i in range(1,len(arr)):
        k=i
        j=i-1
        while j>=0 and arr[k]<arr[j]:
            arr[j],arr[k]=arr[k],arr[j]
            k=j
            j=j-1

    print(arr)
arr=[12, 11, 13, 5, 6]
insertion_sort(arr)

# ---------------------------------------------------------------------
# BY FOR LOOP
n=[14,46,43,27,57,41,45,21,70]  # [14, 21, 27, 41, 43, 45, 46, 57, 70]
for i in range(1,len(n)):
    for j in range(0,len(n)-1):
        key =j+1
        if n[j]>n[key]:
            n[j],n[key]=n[key],n[j]
print(n)