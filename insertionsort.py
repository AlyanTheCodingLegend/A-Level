# bubble sort

userarray=[4,2,8,6,7,9,1,3,7,5,6,2]

# start index
# end index
# mid index is the average of start and end

def bubbleSort(arr):
     
    n=len(arr) # n=14

    for i in range(n): # 0 - (n-1)

        swapped=False

        for j in range(0,(n-1)-i):
            
            # if n is the length, n-1 is the index of the LAST element
            
            if arr[j] > arr[j+1]: # we shall swap if true
                
                arr[j], arr[j+1] = arr[j+1], arr[j]

                # temp=arr[j+1]
                # arr[j+1]=arr[j]
                # arr[j] = temp 

                swapped = True # swapping has been done

        if swapped==False:
            break

    return arr

print("Bubble Sort: ")
print(bubbleSort(userarray))


def insertionSort(arr):

    # index = 0, assume that first element is already sorted (kindof)

    n=len(arr)

    for i in range(1, n): # i-> 1 till len(arr)-1
        # key = arr[7]
        key = arr[i] # key stores 2nd element onwards

        # Move elements of arr[0..(i-1)] which are greater than the key
        # move them one position ahead of their current position

        j=i-1  # j-> 0 till len(arr) - 2
        # j=6

        while j>=0 and key < arr[j]:
        
            arr[j+1] = arr[j] # arr[1] = arr[0]

            j=j-1 # will not run

        arr[j+1]=key # arr[7] = arr[7]   

    return arr    


# arr = [5,2,9,8,0]
    
# i=1, j=0, key= 2, arr[j] = 5, arr[j+1] = 5, j=-1, loop exits, arr[0]=2
# [2,5,9,8,0] swap 1

# i=2, j=1, key = 9, arr[j] = 5, arr[j+1]=9
# [2,5,9,8,0] swap 0 
        
# [2,5,8,9,0] swap 1
        
# [0,2,5,8,9] our final pass is complete
        
print("Insertion Sort: ")        
print(insertionSort(userarray))