Implementation Details:
Heap Sort begins by transforming the input array into a max-heap using the heapify function. The heapify process ensures that each parent node is larger than its children. Once the array is heapified, the sorting process involves repeatedly swapping the root (largest element) with the last element of the heap and reducing the heap size by one. The heap property is then restored through the heapify process, which is called for the root element. This continues until all elements have been sorted. The heapify operation and sorting process both run in O(log n) time, and since each element is processed once, the overall time complexity of the algorithm remains O(n log n). Additionally, the algorithm sorts in place without requiring additional memory, which optimizes space usage.

Time Complexity:
The total time it takes to build the heap is linear O(n) where as the heapify depends on the level of tree which is O(log n) giving us a total of O(n log n) time to build the max heap. Since every step includes swapping the root with largest all worst, best and average case gives same time complexity.

Space Complexity:
The space complexity is constant O(1) since it doesn't require additional memory to stor data.

Result Comparison of Quick Sort vs Merge Sort vs Heap Sort:
Input Type	                  Quick Sort Time	        Merge Sort Time	        Heap Sort Time
Sorted Array    	          3.62e-05 seconds	        3.17e-05 seconds	    1.98e-05 seconds
Sorted Reverse Array	      3.41e-05 seconds	        3.17e-05 seconds	    1.31e-05 seconds
Sorted Random Array (1000)	   0.00222 seconds      	0.00258 seconds     	0.00235 seconds

The results aligns with the theoretical analysis of each algorithm's time complexity. Quick Sort, with an average-case time complexity of O(n log n), performs the fastest on random input due to its efficient partitioning strategy. However, it slow downs to sorted and reverse-sorted arrays. Merge Sort, with a consistent O(n log n) time complexity, behaves predictably across all input distributions, making it stable but slightly slower than Quick Sort for random input due to its additional memory overhead for merging. Heap Sort performs well across all types of input, especially sorted and reverse-sorted arrays, due to its O(n log n) time complexity in every case and O(1) space complexity, though it tends to be slower than Quick Sort for random input, likely due to its less cache-efficient nature.

