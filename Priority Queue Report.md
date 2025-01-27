Design Choices:
Data Structure: Binary Heap (Array-based): I chose a max-heap to prioritize tasks with higher priority (larger values). The binary heap is implemented using an array because it provides efficient access to parent and child nodes through simple index arithmetic and minimizes memory overhead compared to tree-based implementations.

Task Representation: The Task class stores essential attributes like task_id, priority, arrival_time, and deadline to represent a task's details, which are crucial for scheduling.

Implementation Details
- insert(task): Adds a task to the heap and restores the heap property by bubbling up the task if needed.
- extract_max(): Removes and returns the highest priority task (root of the heap) and restores the heap property by bubbling down.
- increase_key(task, new_priority): Increases a task's priority and restores the heap property by bubbling up.
- is_empty(): Checks if the heap is empty (constant time operation).
- _heapify_up(): Restores the heap property by moving a task up the heap.
- _heapify_down(): Restores the heap property by moving a task down the heap.
- _find_task_index(): Finds a task's index by its task_id.

Time Complexity Analysis
insert(task): O(log n) – The task is added, and the heap property is restored by bubbling up.
extract_max(): O(log n) – The root task is removed, and the heap property is restored by bubbling down.
increase_key(task, new_priority): O(log n) – The task's priority is updated, and the heap property is restored.
is_empty(): O(1) – Simply checks the size of the heap.