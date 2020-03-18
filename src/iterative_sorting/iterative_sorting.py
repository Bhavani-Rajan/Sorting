# TO-DO: Complete the insertion_sort() function below
def insertion_sort( arr ):
#Separate the first element from the rest of the array. Think about it as a sorted list of one element.

    #For all other indices, beginning with [1]:
    for elem in range(1,len(arr)):
        # Copy the item at that index into a temp variable
        temp = arr[elem]
        # Iterate to the left until you find the correct index in the "sorted" part of the array 
        # at which this element should be inserted  
        for i in range(len(l[:elem])):
        #   - Shift items over to the right as you iterate
    
        #   c. When the correct index is found, copy temp into this position
            if(temp < arr[i]):
                arr.pop(elem)
                arr.insert(i,temp)
                break;




# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index 
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        smallest_index += arr[i:].index(min(arr[i:]))



        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index] 
        




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    
    swap_occured=True
    while(swap_occured):
        swap_occured=False
        for index in range(len(arr) - 1):
            if(arr[index] > arr[index+1]):
                arr[index] , arr[index+1] = arr[index+1], arr[index]
                swap_occured=True  
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr