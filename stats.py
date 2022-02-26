class Stats():
    """отслеживание статистики"""

    def __init__(self):
        """инициализируем статистику"""
        self.reset_stats()
        self.run_game = True
        with open('high_score.txt', 'r') as file:
            self.high_score = int(file.readline())

    def reset_stats(self):
        """статистика изменений в игре"""
        self.guns_left = 2
        self.score = 0