# Stacks or pyramids

### Task Description

Imagine you're given the following problem in a technical interview, and you need to solve it using a heap.

You have several network cables of different lengths that need to be combined two at a time into a single cable using connectors. The cost of connecting two cables is equal to the sum of their lengths, and the total cost is the sum of all such connections.

The task is to find the order of combining the cables that minimizes the total cost.

### Optional Task

You are given k sorted lists of integers. Your task is to merge them into a single sorted list. You should use a min-heap to efficiently merge multiple sorted lists into one sorted list. Implement a function merge_k_lists that takes a list of sorted lists as input and returns a sorted list.

Example of Expected Output:

```python
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Sorted list:", merged_list)
```

```less
Sorted list: [1, 1, 2, 3, 4, 4, 5, 6]
```
