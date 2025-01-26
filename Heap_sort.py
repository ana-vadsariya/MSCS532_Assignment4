import random
import time

def heapify(arr, n, i):
    # Since its max heap root will be the largest
    largest = i
    #index for left child
    left_child = 2*i+1 
    #3index for right child
    right_child = 2*i+2 

    # If left child is larger than root make left the largest value
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    # If right child is larger than the largest so far make right the largest value
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    # Check if largest is not root
    if largest != i:
        #if not swap it
        arr[i], arr[largest] = arr[largest], arr[i]
        #call heapify to continue sorting 
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    
    # Build the max-heap
    # Start from the last non-leaf node (n//2 - 1) and heapify each node
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap one by one and place them at the end of the array
    for i in range(n - 1, 0, -1):
        # Swap the root which is the largest element with the last element
        arr[i], arr[0] = arr[0], arr[i]       
        # Heapify the reduced heap
        heapify(arr, i, 0)
    return arr

# Quick Sort Implementation Using Recusion grabbed code from Assignment 2
def quick_sort(arr):
    #Base case which stops the recursion when length of array becomes 1 or 0.
    if len(arr) <= 1:
        return arr
    #Randomly select pivot from the array starting at position 0 till the last element
    pivot = arr[random.randint(0, len(arr) - 1)]
    #all the values smaller than pivot goes to left_Side list
    left_side = [x for x in arr if x < pivot]
    #here is the pivot
    pivot_valeu = [x for x in arr if x == pivot]
    #all the values greater than pivot goes to right_Side list
    right_side = [x for x in arr if x > pivot]
    #now we send the left_side + pivot + right_side back to the recursion
    return quick_sort(left_side) + pivot_valeu + quick_sort(right_side)

# Merge Sort Implementation Using Recusion grabbed code from Assignment 2
def merge_sort(arr):
    #Base case which stops the recursion when length of array becomes 1 or 0.
    if len(arr) <= 1:
        return arr 
    # Divide the array into two equally parts 
    mid = len(arr) // 2
    #Extract the values before mid-point and add it to left_side array 
    left_side = arr[:mid]
    #Extract the values after mid-point and add it to right_side array 
    right_side = arr[mid:]
    #send both sides to the recursion level and store then in their respective variables
    left_sorted = merge_sort(left_side)
    right_sorted = merge_sort(right_side)
    # Merge the two sorted halves
    return merge(left_sorted, right_sorted)

#Merge step grabbed code from Assignment 2
def merge(left, right):
    merged = []
    i = j = 0
    # Merge the two lists in sorted order
    while i < len(left) and j < len(right):
        #Comparison is done to idenitfy which element to add next in the array
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # Append any remaining elements from both halves
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# Measure execution time of a function grabbed code from Assignment 2
def measure_time(func, arr):
    start_time = time.time()
    result = func(arr)
    end_time = time.time()
    return result, end_time - start_time

#compare quick. merge and heap sort grabbed code from Assignment 2
def test_sorting_algorithms():
    array_sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    array_reverse_sorted = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    array_random = random.sample(range(1, 10000), 1000)  

    #Quick Sort for sorted array
    quick_sorted, quick_time = measure_time(quick_sort, array_sorted)
    print("Sorted Array using Quick Sort") 
    print("Quick Sort Time:", quick_time, "seconds")
    print()
        
    #Merge Sort for sorted array
    merge_sorted, merge_time = measure_time(merge_sort, array_sorted)
    print("Sorted Array using Merge Sort") 
    print("Merge Sort Time:", merge_time, "seconds")
    print()

    #Heap Sort for sorted array
    heap_sorted, heap_time = measure_time(heap_sort, array_sorted)
    print("Sorted Array using Heap Sort") 
    print("Heap Sort Time:", heap_time, "seconds")
    print()

    #Quick Sort for reverse sorted array
    quick_sorted, quick_time = measure_time(quick_sort, array_reverse_sorted)
    print("Sorted Reverse Array using Quick Sort") 
    print("Quick Sort Time:", quick_time, "seconds")
    print()

    #Merge Sort for reverse sorted array
    merge_sorted, merge_time = measure_time(merge_sort, array_reverse_sorted)
    print("Sorted Reverse Array using Merge Sort") 
    print("Merge Sort Time:", merge_time, "seconds")
    print()

    #Heap Sort for reverse sorted array
    heap_sorted, heap_time = measure_time(heap_sort, array_reverse_sorted)
    print("Sorted Reverse Array using Heap Sort") 
    print("Heap Sort Time:", heap_time, "seconds")
    print()

    #Quick Sort for random array
    quick_sorted, quick_time = measure_time(quick_sort, array_random)
    print("Sorted Random Array of size 1000 using Quick Sort") 
    print("Quick Sort Time:", quick_time, "seconds")
    print()
        
    #Merge Sort for random array
    merge_sorted, merge_time = measure_time(merge_sort, array_random)
    print("Sorted Random Array of size 1000 using Merge Sort") 
    print("Merge Sort Time:", merge_time, "seconds")
    print()

    #Heap Sort for random array
    heap_sorted, heap_time = measure_time(heap_sort, array_random)
    print("Sorted Random Array of size 1000 using Heap Sort") 
    print("Heap Sort Time:", heap_time, "seconds")
    print()

arr = [12, 11, 13, 5, 6, 7]
sorted_arr = heap_sort(arr)
print(f"Sorted Array After using Heap Sort: {sorted_arr}")
print()
print("Comparison of Quick Sort vs Merge Sort vs Heap Sort:")
print()
test_sorting_algorithms()
