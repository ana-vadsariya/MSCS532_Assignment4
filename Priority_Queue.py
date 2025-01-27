# Task class to represent a task with task_id, priority, arrival_time, and deadline.
class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):        
        #Unique identifier for the task.
        self.task_id = task_id
        #higher value means higher priority
        self.priority = priority
        #The time at which the task arrives.
        self.arrival_time = arrival_time
        #The time by which the task should be completed.
        self.deadline = deadline
        
    def __repr__(self):
        return f"Task(id={self.task_id}, priority={self.priority}, arrival_time={self.arrival_time}, deadline={self.deadline})"

class PriorityQueue:
    def __init__(self):
        #Initialize an empty priority queue.
        #The heap will store the tasks, and we will maintain the heap property (max-heap).
        self.heap = []
    
    def insert(self, task):
        #Insert a new task into the priority queue while maintaining the max-heap property.
        # Add task to the end of the heap
        self.heap.append(task)  
        # Ensure heap property is maintained
        self._heapify_up(len(self.heap) - 1)  
    
    def _heapify_up(self, index):
        #Restore the heap property by "bubbling up" the element at the given index.
        
        #Index of the task to bubble up.
        while index > 0:
            parent_index = (index - 1) // 2
            # If the current task has higher priority than its parent, swap them
            if self.heap[index].priority > self.heap[parent_index].priority:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    #Remove and return the task with the highest priority (the root of the heap).
    def extract_max(self):      
        #Rebalance the heap by "heapifying down".
        #Task with the highest priority or None if the heap is empty.
        if len(self.heap) == 0:
            return None
        
        # The root task is the one with the highest priority
        max_task = self.heap[0]
        
        # Replace the root with the last element and remove the last element
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        
        # Restore the heap property by heapifying down
        self._heapify_down(0)
        
        return max_task
    
    def _heapify_down(self, index):
       #Restore the heap property by "bubbling down" the element at the given index.
        n = len(self.heap)
        # While there is at least one child
        while 2 * index + 1 < n:  
            left_child_index = 2*index+1
            right_child_index = 2*index+2
            largest = index
            
            # Check if left child has higher priority than current node
            if left_child_index < n and self.heap[left_child_index].priority > self.heap[largest].priority:
                largest = left_child_index
            # Check if right child has higher priority than current node
            if right_child_index < n and self.heap[right_child_index].priority > self.heap[largest].priority:
                largest = right_child_index
            
            # If the largest element is not the current element, swap them
            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break
    
    def increase_key(self, task, new_priority):
        #The task whose priority is to be increased assign new priority of the task.
        task.priority = new_priority
        index = self._find_task_index(task)
        if index != -1:
            self._heapify_up(index)
    
    def _find_task_index(self, task):
        #Find the index of a task in the heap by its task_id.    
        for i, t in enumerate(self.heap):
            if t.task_id == task.task_id:
                return i
        return -1
    
    def is_empty(self):
       #returns true is empty
        return len(self.heap) == 0
    
    def __repr__(self):
        return f"PriorityQueue({self.heap})"

if __name__ == "__main__":
    # Create a few tasks
    task1 = Task(1, priority=5, arrival_time=1, deadline=10)
    task2 = Task(2, priority=3, arrival_time=2, deadline=8)
    task3 = Task(3, priority=8, arrival_time=3, deadline=6)
    task4 = Task(4, priority=2, arrival_time=4, deadline=7)
    
    # Initialize the priority queue (max-heap)
    pq = PriorityQueue()
    
    # Insert tasks into the priority queue
    pq.insert(task1)
    pq.insert(task2)
    pq.insert(task3)
    pq.insert(task4)
    
    # Extract tasks from the queue in order of priority
    print("Priority Queue after insertion:")
    print(pq)
    
    print("\nExtracting tasks:")
    print(pq.extract_max())  # Should return task3 (priority 8)
    print(pq.extract_max())  # Should return task1 (priority 5)
    print(pq.extract_max())  # Should return task2 (priority 3)
    print(pq.extract_max())  # Should return task4 (priority 2)
    
    # Check if the priority queue is empty
    print("\nIs the priority queue empty?")
    print(pq.is_empty())  # Should return True
