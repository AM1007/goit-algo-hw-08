import heapq

def merge_k_lists(lists):
    min_heap = []
    result = []

    # Ініціалізуємо мін-кучу з перших елементів кожного списку
    for i, lst in enumerate(lists):
        if lst:  # Перевіряємо, чи список не пустий
            heapq.heappush(min_heap, (lst[0], i, 0))  # (значення, індекс списку, індекс елемента в списку)
    
    # Виймаємо мінімальні елементи і додаємо їх у результат
    while min_heap:
        val, list_idx, element_idx = heapq.heappop(min_heap)
        result.append(val)
        
        # Якщо є наступний елемент у цьому списку, додаємо його в купу
        if element_idx + 1 < len(lists[list_idx]):
            next_tuple = (lists[list_idx][element_idx + 1], list_idx, element_idx + 1)
            heapq.heappush(min_heap, next_tuple)
    
    return result

# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
