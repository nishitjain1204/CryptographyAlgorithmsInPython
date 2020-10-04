# Re-arrange the heap to maintain the heap property - I.e. 'Heapify' With n being the size of the heap & i being the largest as the root
def main(arr, n, i): 
    largest = i  
    left = 2 * i + 1     
    right = 2 * i + 2    
    
    # Check if the left child of the root exists and is greater than the root 
    if left < n and arr[i] < arr[left]: 
        largest = left

    # Check if the right child of the root exists and is greater than the root 
    if right < n and arr[largest] < arr[right]: 
        largest = right

    # Change the root if i was not the largest
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] 
        # 'Heapify the root'
        main(arr, n, largest) 

# Function to sort the given array
def HeapSort(arr): 
    n = len(arr) 
    
    # Build a Max Heap
    for i in range(n // 2 - 1, -1, -1): 
        main(arr, n, i) 
    
    # Extract the elements one by one
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]  
        main(arr, i, 0)   

    # Print out the sorted array
    n = len(array) 
    print ("The Sorted Array Is:") 
    for i in range(n): 
        print ("%d" %array[i]) 

if __name__ == "__main__":
    print("Please Enter The Elements One After The Other Separated By A Space:")
    array = list(map(int,input().split()))
    HeapSort(array)
