def mergesort_recursive(arr):
    if len(arr)>1:
        print(arr)
        m = len(arr) // 2
        left = arr[:m]
        right = arr[m:]
        #RECURSIVE PART
        mergesort_recursive(left)
        mergesort_recursive(right)
        # i,j,k USE FOR INDEXING
        i=j=k=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k]=left[i]
                i=i+1
                # k=k+1
            else:
                arr[k]=right[j]
                j=j+1
                # k=k+1
            k=k+1 #(THIS K+=1 IS FOR BOTH I & J)if i is true the i will be increment and after i the k also increment
        # this is for rest of the ith element in the single element list is copied it into list
        while i < len(left):
            arr[k]=left[i]
            i=i+1
            k=k+1
        # this is for rest of the jth element in the single element list is copied it into list
        while j < len(right):
            arr[k]=right[j]
            j=j+1
            k=k+1

    print(arr)

unsorted_arr=[3,4,2,1,6,5]
mergesort_recursive(unsorted_arr)