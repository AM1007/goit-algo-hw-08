import heapq

def min_cost_to_connect_cables(cables):
    # Перетворимо список кабелів у мін-кучу
    heapq.heapify(cables)
    
    total_cost = 0
    
    # Поки у нас є більше ніж один кабель
    while len(cables) > 1:
        # Виймаємо два найкоротші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Об'єднуємо їх, вартість об'єднання додається до загальних витрат
        combined_length = first + second
        total_cost += combined_length
        
        # Додаємо новий об'єднаний кабель назад у купу
        heapq.heappush(cables, combined_length)
    
    return total_cost

# Приклад використання
cables = [4, 3, 2, 6]
print(min_cost_to_connect_cables(cables))  # Вихід: 29
