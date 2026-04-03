import random
from tasks import tasks

def get_task_by_mood(mood_level):
    """
    Получает задание по выбранной категории настроения
    mood_level: int 1-3, 4-6, 7-10
    """
    mood_level = max(1, min(10, mood_level))
     
    if mood_level <= 3:
        possible_levels = [1, 2, 3]
    elif mood_level <= 6:
        possible_levels = [4, 5, 6]
    elif mood_level <= 9:
        possible_levels = [7, 8, 9]
    else:
    	possible_levels = [10]
    
    # Выбираем случайный уровень из диапазона
    level = random.choice(possible_levels)
    # Выбираем случайное задание из этого уровня
    return random.choice(tasks[level])