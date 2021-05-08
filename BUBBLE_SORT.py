def bubbleSort(array):
    count = 0
    for i in range(len(array)-1):
        if array[i] > array[i + 1]:
            array[i],array[i + 1] = array[i + 1],array[i] #swap
            count += 1 #condition is true then count will be +1
    # after exit the loop, it checks the below if condition till count will be 0.if count is 0 then it prints sorted array
    if count == 0:
        return array
    else:
        # recusion
        return bubbleSort(array)

arr = [1,5,2,7,3]
print(arr)
print(bubbleSort(arr))