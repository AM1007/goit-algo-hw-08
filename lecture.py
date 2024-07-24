# Зберігання купи в списку
# import heapq

# nums = [4, 10, 3, 5, 1]
# # Перетворення іттерабельного елемента у купу
# heapq.heapify(nums)
# print("heapify:",nums)
# # Додавання елементу до та перетворення купи
# heapq.heappush(nums, 0)
# print("heappush:",nums)
# # Видалення та повернення найменьшого елемента з купи
# min_elem = heapq.heappop(nums)
# print(min_elem)  # Output: 0
# print("heappop:",nums)
# # Додавання елементу до купи та повернення найменьшего елемента
# min_elem = heapq.heappushpop(nums, 2)
# print(min_elem)  # Output: 1
# print("heappushpop:", nums)
# # Видалення елемента з купи та повернення найменьшого елемента
# min_elem = heapq.heapreplace(nums, 0)
# print(min_elem)  # Output: 2
# print("heapreplace:", nums)
# # Повернення найбільшого та найменшого елементів
# largest_three = heapq.nlargest(3, nums)
# smallest_three = heapq.nsmallest(3, nums)
# print("largest_three:", largest_three)  # Output: [10, 5, 4]
# print("smallest_three:",smallest_three)  # Output: [0, 3, 4]
# print(nums)

# ===========================

# Черги з пріорітетами

# def convert_image(file_name, target_format):
#     # Припустимо, що ця функція конвертує зображення (тут просто імітація)
#     print(f"Конвертація {file_name} до {target_format} формату...")
#     return f"{file_name.split('.')[0]}.{target_format}"

# import heapq

# class PriorityQueue:
#     def __init__(self):
#         self.queue = []

# # Вставка
#     def enqueue(self, task, priority):
#         heapq.heappush(self.queue, (-priority, task))

# # Видалення
#     def dequeue(self):
#         return heapq.heappop(self.queue)[1]
    
# # Обробка
#     def is_empty(self):
#         return not bool(self.queue)

# ===========================

# Пірамідальне сортування

# import heapq

# def heap_sort(iterable, descending=False):
#     # Визначаємо, який знак використовувати залежно від порядку сортування
#     sign = -1 if descending else 1

# 		# Створюємо купу, використовуючи заданий порядок сортування
#     h = [sign * el for el in iterable]
#     heapq.heapify(h)
#     # Витягуємо елементи, відновлюємо їхні оригінальні значення (якщо потрібно) і формуємо відсортований масив
#     return [sign * heapq.heappop(h) for _ in range(len(h))]

# # Приклади використання функції
# arr = [12, 11, 13, 5, 6, 7]
# # Сортування за зростанням (за замовчуванням)
# sorted_arr_asc = heap_sort(arr)
# print("Відсортований масив (за зростанням):", sorted_arr_asc)
# # Сортування за спаданням
# sorted_arr_desc = heap_sort(arr, descending=True)
# print("Відсортований масив (за спаданням):", sorted_arr_desc)

